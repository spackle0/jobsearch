from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommunicationLogForm
from .models import CommunicationLog, Company


def company_list(request):
    companies = Company.objects.all()
    return render(request, "interviews/company/company_list.html", {"companies": companies})


def company_detail(request, id):
    company = get_object_or_404(Company, pk=id)
    return render(request, "interviews/company/company_detail.html", {"company": company})


def communication_log_list(request):
    communication_logs = CommunicationLog.objects.all()
    return render(
        request, "interviews/communicationlog/communicationlog_list.html", {"communication_logs": communication_logs}
    )


def communication_log_detail(request, id):
    communication_log = get_object_or_404(CommunicationLog, pk=id)
    return render(
        request, "interviews/communicationlog/communicationlog_detail.html", {"communication_log": communication_log}
    )


def communication_log_add(request):
    if request.method == "POST":
        form = CommunicationLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("communication_log_list")  # Adjust the redirect to your list view's name
    else:
        form = CommunicationLogForm()
    return render(request, "interviews/communicationlog/communicationlog_add_edit.html", {"form": form})


def communication_log_edit(request, id):
    communication_log = get_object_or_404(CommunicationLog, pk=id)
    if request.method == "POST":
        form = CommunicationLogForm(request.POST, instance=communication_log)
        if form.is_valid():
            form.save()
            return redirect("communication_log_detail", id=id)  # Adjust as necessary
    else:
        form = CommunicationLogForm(instance=communication_log)
    return render(
        request,
        "interviews/communicationlog/communicationlog_add_edit.html",
        {"form": form, "communication_log": communication_log},
    )
