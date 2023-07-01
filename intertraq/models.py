from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Recruiter(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = PhoneNumberField(region="US", blank=True)
    company = models.ForeignKey("Company", on_delete=models.SET_NULL, null=True, blank=True)
    is_independent = models.BooleanField()

    def __str__(self):
        return f"{self.name} ({self.company.name})"


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    industry = models.CharField(max_length=100, blank=True)
    phone_number = PhoneNumberField(region="US", blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    job_url = models.URLField(max_length=200, null=True, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    recruiter = models.ForeignKey("Recruiter", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title} ({self.company.name})"


class Interview(models.Model):
    job = models.ForeignKey("Job", on_delete=models.CASCADE)
    purpose = models.CharField(max_length=200)
    date = models.DateTimeField()
    attendees = models.ManyToManyField("Recruiter", blank=True)
    virtual_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"Interview for {self.job.title} on {self.date}"


class CommunicationLog(models.Model):
    date = models.DateField(default=timezone.now)
    recruiter = models.ForeignKey("Recruiter", on_delete=models.CASCADE)
    job = models.ForeignKey("Job", on_delete=models.CASCADE, null=True, blank=True)
    log_entry = models.TextField()

    def __str__(self):
        return f"{self.date:%Y-%m-%d}: {self.recruiter.name} - {self.log_entry[:50]}"
