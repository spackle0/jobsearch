from django.urls import path
from django.views.generic import TemplateView

from .views import (
    CompanyCreateView,
    CompanyDetailView,
    CompanyListView,
    CompanyUpdateView,
    JobCreateView,
    JobDetailView,
    JobListView,
    JobUpdateView,
    RecruiterCreateView,
    RecruiterDetailView,
    RecruiterListView,
    RecruiterUpdateView,
)

urlpatterns = [
    # Index
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    # Jobs
    path("create-job/", JobCreateView.as_view(), name="create-job"),
    path("jobs/", JobListView.as_view(), name="jobs"),
    path("job/<int:pk>/", JobDetailView.as_view(), name="job-detail"),
    path("job/<int:pk>/edit/", JobUpdateView.as_view(), name="job-update"),
    # Companies
    path("create-company/", CompanyCreateView.as_view(), name="create-company"),
    path("companies/", CompanyListView.as_view(), name="companies"),
    path("company/<int:pk>/", CompanyDetailView.as_view(), name="company-detail"),
    path("company/update/<int:pk>/", CompanyUpdateView.as_view(), name="company-update"),
    # Recruiters
    path("create-recruiter/", RecruiterCreateView.as_view(), name="create-recruiter"),
    path("recruiters/", RecruiterListView.as_view(), name="recruiters"),
    path("recruiter/<int:pk>/", RecruiterDetailView.as_view(), name="recruiter-detail"),
    path("recruiter/update/<int:pk>/", RecruiterUpdateView.as_view(), name="recruiter-update"),
]
