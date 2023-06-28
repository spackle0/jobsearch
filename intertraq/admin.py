from django.contrib import admin

from .models import CommunicationLog, Company, Interview, Job, Recruiter


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Recruiter)
class RegisterAdmin(admin.ModelAdmin):
    pass


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(CommunicationLog)
class CommunicationLogAdmin(admin.ModelAdmin):
    fields = ("date", "recruiter", "job", "message")
    search_fields = ["date", "job__title", "recruiter__name"]
    list_display = ("date", "recruiter", "job", "message")
