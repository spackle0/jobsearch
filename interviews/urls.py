from django.urls import path

from .views import communication_log_detail, communication_log_list, company_detail, company_list

app_name = "interviews"

urlpatterns = [
    path("companies/", company_list, name="company_list"),
    path("companies/<int:id>/", company_detail, name="company_detail"),
    path("communication-logs/", communication_log_list, name="communication_log_list"),
    path("communication-logs/<int:id>/", communication_log_detail, name="communication_log_detail"),
]
