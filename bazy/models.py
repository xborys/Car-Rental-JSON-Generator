from django.db import models

class Client(models.Model):
    name = models.CharField('Name', max_length=100)
    lastname = models.CharField('Lastname', max_length=100)
    address = models.CharField('Address', max_length=100)
    postal_code = models.CharField('Postal code', max_length=6)
    city = models.CharField('City', max_length=100)
    phone = models.IntegerField('Phone number')
    PESEL = models.IntegerField('PESEL number')
    credit_card_number = models.CharField('Credit card number', max_length=16)
    credit_card_expiration_date = models.CharField('Credit card expiration date', max_length=5, help_text='Enter the credit card expiration date (MM/YY)')
    credit_card_CVV = models.CharField('Credit card CVV', max_length=3)

    def __str__(self):
        return str(self.name) + ' ' + str(self.lastname)

class Employee(models.Model):
    name = models.CharField('Name', max_length=100)
    lastname = models.CharField('Lastname', max_length=100)
    mail = models.EmailField('E-mail')
    phone = models.IntegerField('Phone number')

    def __str__(self):
        return self.name + ' ' + self.lastname

class Car_Type(models.Model):
    classes = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('SUV', 'SUV'),
        ('M', 'M'),
        ('S', 'S'),
    ]

    seats = [
        ('2', '2'),
        ('4', '4'),
        ('5', '5'),
        ('7', '7'),
    ]

    fuel = [
        ('petrol', 'petrol'),
        ('diesel', 'diesel'),
        ('electric', 'electric'),
        ('hybrid', 'hybrid'),
    ]

    classes = models.CharField('Class', max_length=3, choices=classes)
    seats = models.CharField('Seats', max_length=1, choices=seats)
    fuel = models.CharField('Fuel', max_length=8, choices=fuel)

    def __str__(self):
        return self.classes + ' ' + self.seats + ' ' + self.fuel
    
class Car_status(models.Model):
    status = [
        ('available', 'available'),
        ('unavailable', 'unavailable'),
    ]

    status = models.CharField('Status', max_length=11, choices=status)

    def __str__(self):
        return self.status
    
class Car(models.Model):

    type_of_drive = [
        ('AWD', 'AWD'),
        ('FWD', 'FWD'),
        ('RWD', 'RWD'),
    ]

    make = models.CharField('Make', max_length=100)
    model = models.CharField('Model', max_length=100)
    engine = models.CharField('Engine', max_length=100)
    type_of_drive = models.CharField('Type of drive', max_length=3, choices=type_of_drive)
    power = models.IntegerField('Power')
    VIN = models.CharField('VIN', max_length=100)
    plate = models.CharField('Plate', max_length=100)
    status = models.ForeignKey(Car_status, on_delete=models.CASCADE)

    def __str__(self):
        return self.make + ' ' + self.model + ' ' + self.plate
    
class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    end_date = models.DateField('End date')

    def __str__(self):
        return self.client + ' ' + self.car + ' ' + self.end_date
    
class Rent(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.client) + ' ' + str(self.car)
    
class Rental_issue(models.Model):
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE)
    date = models.DateField('Date')

    def __str__(self):
        return str(self.rent) + ' ' + str(self.date)
    
class Rental_return(models.Model):
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE)
    date = models.DateField('Date')

    def __str__(self):
        return str(self.rent) + ' ' + str(self.date)
    
class Rental_bill(models.Model):
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    fv_number = models.IntegerField('FV number')
    date = models.DateField('Date')
    amount = models.IntegerField('Amount')

    def __str__(self):
        return f"{self.rent} {self.client} {self.employee} {self.fv_number} {self.date} {self.amount}"
