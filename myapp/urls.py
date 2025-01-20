from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculate-percentage/', views.calculate_percentage, name='calculate_percentage'),
    path('cli_view/', views.cli_view, name='cli_view'),
]
