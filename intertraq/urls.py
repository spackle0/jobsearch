from django.urls import path
from . import views

urlpatterns = [
    # other URL patterns
    path('appointments/', views.appointments, name='appointments'),
]
