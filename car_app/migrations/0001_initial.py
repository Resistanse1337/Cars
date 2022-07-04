# Generated by Django 4.0.6 on 2022-07-04 12:11

import car_app.utils
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('registration_number', models.CharField(max_length=255)),
                ('release_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), car_app.utils.max_value_current_year])),
                ('vin', models.CharField(max_length=255)),
                ('sts_number', models.CharField(max_length=255)),
                ('sts_date', models.DateField()),
            ],
        ),
    ]