from django.contrib import admin

from .models import CommunicationLog, Company, Interview, Job, Recruiter


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    pass


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(CommunicationLog)
class CommunicationLogAdmin(admin.ModelAdmin):
    @admin.display(description="Date")
    def date_display(self, obj):
        return obj.date.strftime("%Y-%m-%d")

    list_display = ("date_display", "recruiter", "job", "comms_type", "log_entry")
    fields = ("date", "recruiter", "job", "comms_type", "log_entry")
    search_fields = ["date", "job__title", "recruiter__name"]
