from django.shortcuts import render


def company_list(request):
    return render(request, 'interviews/company/list.html', {})