from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views

register_converter(FourDigitYearConverter, 'yyyy')


app_name = 'shop'

urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year),
]