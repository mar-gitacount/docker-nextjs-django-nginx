from django.urls import path,include
from .views import usaBuchererexcution

urlpatterns = [
    path('usaBucherer/', usaBuchererexcution, name='usaBuchererexcution'),
]