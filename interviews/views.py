from django.shortcuts import render, get_object_or_404

from .models import Company


def company_list(request):
    companies = Company.objects.all()
    return render(request, "interviews/company/company_list.html", {'companies': companies})


def company_detail(request, id):
    company = get_object_or_404(Company, pk=id)
    return render(request, 'interviews/company/company_detail.html', {'company': company})
