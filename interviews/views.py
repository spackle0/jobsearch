from django.shortcuts import get_object_or_404, render

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
