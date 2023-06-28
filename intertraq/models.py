# Third Party Libraries
from django.db import models


class Recruiter(models.Model):
    name = models.CharField(max_length=200)
    is_independent = models.BooleanField()
    company = models.ForeignKey("Company", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    industry = models.CharField(max_length=100, blank=True)

    # new fields
    phone_number = models.CharField(max_length=15, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    recruiter = models.ForeignKey("Recruiter", on_delete=models.SET_NULL, null=True)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Interview(models.Model):
    job = models.ForeignKey("Job", on_delete=models.CASCADE)
    purpose = models.CharField(max_length=200)
    date = models.DateTimeField()
    attendees = models.ManyToManyField("Recruiter", blank=True)

    def __str__(self):
        return f"Interview for {self.job.title} on {self.date}"


class CommunicationLog(models.Model):
    recruiter = models.ForeignKey("Recruiter", on_delete=models.CASCADE)
    job = models.ForeignKey("Job", on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return f"{self.recruiter.name} - {self.message[:50]}..."
