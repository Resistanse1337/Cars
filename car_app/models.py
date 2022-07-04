from django.core.validators import MinValueValidator
from django.db import models

from car_app.utils import max_value_current_year


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    mark = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=255)
    release_year = models.IntegerField(validators=[MinValueValidator(1900), max_value_current_year])
    vin = models.CharField(max_length=255)
    sts_number = models.CharField(max_length=255)
    sts_date = models.DateField()

