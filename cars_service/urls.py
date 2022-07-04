from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from car_app.views import *


router = routers.SimpleRouter()
router.register("", CarsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path("cars/", include(router.urls))
]
