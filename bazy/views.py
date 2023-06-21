from django.shortcuts import render, redirect
from .models import Client, Employee, Car, Car_status, Reservation, Rent, Rental_issue, Rental_return, Rental_bill, Car_Type
from .forms import ImportForm
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.core import serializers
from faker import Faker
from faker_vehicle import VehicleProvider
import random
import json

def index(request):
    return render(request, 'index.html', {})

def clients(request):
    clients_list = Client.objects.all()

    return render(request, 'clients.html',
                  {'clients_list' : clients_list })

def export_clients_json(request):
    clients = Client.objects.all()
    clients_data = serializers.serialize('json', clients, indent=4)

    response = HttpResponse(clients_data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="clients.json"'

    return response

def import_clients(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            json_file = request.FILES['json_file']
            try:
                json_data = json.load(json_file)
                clients = []
                for item in json_data:
                    client_data = item['fields']
                    client = Client(
                        name=client_data['name'],
                        lastname=client_data['lastname'],
                        address=client_data['address'],
                        postal_code=client_data['postal_code'],
                        city=client_data['city'],
                        phone=client_data['phone'],
                        PESEL=client_data['PESEL'],
                        credit_card_number=client_data['credit_card_number'],
                        credit_card_expiration_date=client_data['credit_card_expiration_date'],
                        credit_card_CVV=client_data['credit_card_CVV']
                    )
                    clients.append(client)
                Client.objects.bulk_create(clients)
                return render(request, 'import_clients.html', {'form': form, 'success': True})
            except json.JSONDecodeError:
                return render(request, 'import_clients.html', {'form': form, 'error': 'Invalid JSON file'})
    else:
        form = ImportForm()
    return render(request, 'import_clients.html', {'form': form})

def generate_clients(request):
    fake = Faker()
    for _ in range(100):
        phone_number = fake.phone_number()  # Generuj losowy numer telefonu
        phone_number_digits = ''.join([c for c in phone_number if c.isdigit()])  # Usuń znaki niebędące cyframi
        phone = int(phone_number_digits)  # Konwertuj na liczbę całkowitą

        client = Client(
            name=fake.first_name(),
            lastname=fake.last_name(),
            address=fake.address(),
            postal_code=fake.postcode(),
            city=fake.city(),
            phone=phone,  # Przypisz prawidłowy numer telefonu
            PESEL=fake.random_number(digits=11),
            credit_card_number=fake.credit_card_number(),
            credit_card_expiration_date=fake.credit_card_expire(start='now', end='+10y', date_format='%m/%y'),
            credit_card_CVV=fake.random_int(min=100, max=999)
        )
        client.save()

    return redirect('clients')

def employees(request):
    employees_list = Employee.objects.all()

    return render(request, 'employees.html',
                  {'employees_list' : employees_list })

def export_employees(request):
    employees = Employee.objects.all()
    data = serializers.serialize('json', employees, indent=4)
    
    response = HttpResponse(data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="employees.json"'
    
    return response

def import_employees(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            json_file = request.FILES['json_file']
            try:
                json_data = json.load(json_file)
                employees = []
                for item in json_data:
                    employee_data = item['fields']
                    employee = Employee(
                        name=employee_data['name'],
                        lastname=employee_data['lastname'],
                        mail=employee_data['mail'],
                        phone=employee_data['phone']
                    )
                    employees.append(employee)
                Employee.objects.bulk_create(employees)
                return render(request, 'import_employees.html', {'form': form, 'success': True})
            except json.JSONDecodeError:
                return render(request, 'import_employees.html', {'form': form, 'error': 'Invalid JSON file'})
    else:
        form = ImportForm()
    return render(request, 'import_employees.html', {'form': form})

def generate_employees(request):
    fake = Faker()
    for _ in range(100):
        phone_number = fake.phone_number()
        phone_number_digits = ''.join([c for c in phone_number if c.isdigit()])
        phone = int(phone_number_digits)

        employee = Employee(
            name=fake.first_name(),
            lastname=fake.last_name(),
            mail=fake.email(),
            phone=phone,
        )
        employee.save()

    return redirect('employees')

def cars(request):
    cars_list = Car.objects.all()

    return render(request, 'cars.html',
                  {'cars_list' : cars_list })

def export_cars(request):
    cars = Car.objects.all()
    data = serializers.serialize('json', cars, indent=4)
    
    response = HttpResponse(data, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="cars.json"'
    
    return response

def import_cars(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            json_file = request.FILES['json_file']
            try:
                json_data = json.load(json_file)
                cars = []
                for item in json_data:
                    car_data = item['fields']
                    status_id = car_data['status']
                    try:
                        status = Car_status.objects.get(id=status_id)
                    except Car_status.DoesNotExist:
                        return render(request, 'import_cars.html', {'form': form, 'error': f'Invalid status ID: {status_id}'})
                    
                    car = Car(
                        make=car_data['make'],
                        model=car_data['model'],
                        engine=car_data['engine'],
                        type_of_drive=car_data['type_of_drive'],
                        power=car_data['power'],
                        VIN=car_data['VIN'],
                        plate=car_data['plate'],
                        status=status
                    )
                    cars.append(car)
                
                Car.objects.bulk_create(cars)
                return render(request, 'import_cars.html', {'form': form, 'success': True})
            
            except json.JSONDecodeError:
                return render(request, 'import_cars.html', {'form': form, 'error': 'Invalid JSON file'})
    
    else:
        form = ImportForm()
    
    return render(request, 'import_cars.html', {'form': form})

def generate_vin():
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]

    vin_without_check_digit = ''.join(random.choices(characters, k=16))

    check_digit = sum(characters.index(vin_without_check_digit[i]) * weights[i] for i in range(16)) % 11
    if check_digit == 10:
        check_digit = 'X'
    else:
        check_digit = str(check_digit)

    return vin_without_check_digit + check_digit

def generate_cars(request):
    engine = ['petrol', 'diesel', 'electric', 'hybrid']
    drive_type = ['FWD', 'RWD', 'AWD']
    fake = Faker()
    fake.add_provider(VehicleProvider)

    for _ in range(100):
        vin = generate_vin()
        car = Car(
            make=fake.vehicle_make(),
            model=fake.vehicle_model(),
            engine=random.choice(engine),
            type_of_drive=random.choice(drive_type),
            power=random.randint(150, 2000),
            VIN=vin,
            plate=fake.license_plate(),
            status=Car_status.objects.get(status='available')
        )
        try:
            car.save()
        except IntegrityError:
            continue

    return redirect('cars')

def preview_json(request):
    if request.method == 'POST':
        json_file = request.FILES['json_file']
        try:
            json_data = json.load(json_file)
            json_str = json.dumps(json_data, indent=4)
            return render(request, 'preview_json.html', {'json_str': json_str})
        except json.JSONDecodeError:
            return render(request, 'preview_json.html', {'error': 'Invalid JSON file'})
    return render(request, 'preview_json.html')

def reservations(request):
    reservations_list = Reservation.objects.all()

    return render(request, 'reservations.html',
                  {'reservations_list' : reservations_list })

def rents(request):
    rents_list = Rent.objects.all()

    return render(request, 'rents.html',
                  {'rents_list' : rents_list })

def rental_issue(request):
    rental_issue_list = Rental_issue.objects.all()

    return render(request, 'rental_issue.html',
                    {'rental_issue_list' : rental_issue_list })

def rental_return(request):
    rental_return_list = Rental_return.objects.all()

    return render(request, 'rental_return.html',
                    {'rental_return_list' : rental_return_list })

def rental_bill(request):
    rental_bill_list = Rental_bill.objects.all()

    return render(request, 'rental_bill.html',
                    {'rental_bill_list' : rental_bill_list })

def car_status(request):
    car_status_list = Car_status.objects.all()

    return render(request, 'car_status.html',
                    {'car_status_list' : car_status_list })

def car_type(request):
    car_type_list = Car_Type.objects.all()

    return render(request, 'car_type.html',
                    {'car_type_list' : car_type_list })