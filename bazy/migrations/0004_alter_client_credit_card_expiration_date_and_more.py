# Generated by Django 4.1.7 on 2023-06-19 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazy', '0003_alter_car_type_of_drive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='credit_card_expiration_date',
            field=models.CharField(help_text='Enter the credit card expiration date (MM/YY)', max_length=5, verbose_name='Credit card expiration date'),
        ),
        migrations.AlterField(
            model_name='client',
            name='credit_card_number',
            field=models.CharField(max_length=16, verbose_name='Credit card number'),
        ),
    ]
