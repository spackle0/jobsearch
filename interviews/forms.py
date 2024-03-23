from django import forms

from .models import CommunicationLog


class CommunicationLogForm(forms.ModelForm):
    class Meta:
        model = CommunicationLog
        fields = ["comms_type", "date", "recruiter", "job", "log_entry", "log_type"]
