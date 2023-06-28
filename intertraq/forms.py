from django import forms

from .models import Company, Job, Recruiter


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["title", "description", "company", "recruiter"]  # Add other fields if needed


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "address", "industry", "phone_number", "website", "email"]


class RecruiterForm(forms.ModelForm):
    class Meta:
        model = Recruiter
        fields = ["name", "is_independent", "company"]
