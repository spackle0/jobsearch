from django.urls import path
from .views import company_list, company_detail

app_name = "interviews"

urlpatterns = [
    path('companies/', company_list, name='company_list'),
    path('companies/<int:id>/', company_detail, name='company_detail'),
]