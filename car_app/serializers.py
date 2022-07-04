from rest_framework import serializers

from car_app.models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
