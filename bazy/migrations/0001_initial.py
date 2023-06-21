# Generated by Django 4.1.7 on 2023-06-19 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100, verbose_name='Make')),
                ('model', models.CharField(max_length=100, verbose_name='Model')),
                ('engine', models.CharField(max_length=100, verbose_name='Engine')),
                ('type_of_drive', models.CharField(max_length=100, verbose_name='Type of drive')),
                ('power', models.IntegerField(verbose_name='Power')),
                ('VIN', models.IntegerField(verbose_name='VIN number')),
                ('plate', models.CharField(max_length=100, verbose_name='Plate')),
            ],
        ),
        migrations.CreateModel(
            name='Car_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable')], max_length=11, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Car_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('SUV', 'SUV'), ('M', 'M'), ('S', 'S')], max_length=3, verbose_name='Class')),
                ('seats', models.CharField(choices=[('2', '2'), ('4', '4'), ('5', '5'), ('7', '7')], max_length=1, verbose_name='Seats')),
                ('fuel', models.CharField(choices=[('petrol', 'petrol'), ('diesel', 'diesel'), ('electric', 'electric'), ('hybrid', 'hybrid')], max_length=8, verbose_name='Fuel')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('lastname', models.CharField(max_length=100, verbose_name='Lastname')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('postal_code', models.CharField(max_length=6, verbose_name='Postal code')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('phone', models.IntegerField(verbose_name='Phone number')),
                ('PESEL', models.IntegerField(verbose_name='PESEL number')),
                ('credit_card_number', models.IntegerField(verbose_name='Credit card number')),
                ('credit_card_expiration_date', models.DateField(verbose_name='Credit card expiration date')),
                ('credit_card_CVV', models.IntegerField(verbose_name='Credit card CVV')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('lastname', models.CharField(max_length=100, verbose_name='Lastname')),
                ('mail', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.IntegerField(verbose_name='Phone number')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazy.car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazy.client')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateField(verbose_name='End date')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazy.car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazy.client')),
            ],
        ),
        migrations.CreateModel(
            name='Rental_return',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazy.rent')),
            ],
        ),
        migrations.CreateModel(
            name='Rental_issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazy.rent')),
            ],
        ),
        migrations.CreateModel(
            name='Rental_bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fv_number', models.IntegerField(verbose_name='FV number')),
                ('date', models.DateField(verbose_name='Date')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazy.client')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazy.employee')),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazy.rent')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazy.car_status'),
        ),
    ]
