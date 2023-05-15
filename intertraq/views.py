from django.http import JsonResponse
from .models import Appointment


def appointments(request):
    appts = Appointment.objects.all()
    appointment_list = []
    for appointment in appts:
        appointment_list.append({
            'id': appointment.id,
            'title': appointment.title,
            'start': appointment.start_time.isoformat(),
            'end': appointment.end_time.isoformat()
        })

    return JsonResponse(appointment_list, safe=False)
