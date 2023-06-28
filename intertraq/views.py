from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView, UpdateView

from .forms import CompanyForm, JobForm, RecruiterForm
from .models import CommunicationLog, Company, Job, Recruiter


# JOBS
class JobListView(ListView):
    model = Job
    template_name = "jobs/job_list.html"  # replace with your template name
    context_object_name = "jobs"
    paginate_by = 10  # if you want pagination


class JobDetailView(DetailView):
    model = Job
    template_name = "jobs/job_detail.html"  # Assuming you have this template in your templates directory
    context_object_name = "job"  # Default is object, you can change it to any name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logs"] = CommunicationLog.objects.filter(job=self.object)
        return context


class JobCreateView(CreateView):
    model = Job
    form_class = JobForm
    template_name = "jobs/job_create.html"
    success_url = "/jobs/"  # replace with your URL

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JobUpdateView(UpdateView):
    model = Job
    template_name = "jobs/job_update.html"  # Assuming you have this template in your templates directory
    form_class = JobForm
    context_object_name = "job"  # Default is object, you can change it to any name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logs"] = CommunicationLog.objects.filter(job=self.object)
        return context


# COMPANIES
class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = "companies/company_create.html"
    success_url = "/companies/"  # replace with your URL


class CompanyListView(ListView):
    model = Company
    template_name = "companies/company_list.html"  # replace with your template name
    context_object_name = "companies"
    paginate_by = 10  # if you want pagination


class CompanyUpdateView(UpdateView):
    model = Company
    fields = ["name", "address", "industry"]
    template_name = "companies/company_update.html"
    context_object_name = "company"

    def get_success_url(self):
        return reverse("company-detail", kwargs={"pk": self.object.pk})


class CompanyDetailView(DetailView):
    model = Company
    template_name = "companies/company_detail.html"  # replace with your template name
    context_object_name = "company"


# RECRUITERS
class RecruiterListView(ListView):
    model = Recruiter
    template_name = "recruiters/recruiter_list.html"  # replace with your template name
    context_object_name = "recruiters"
    paginate_by = 10  # if you want pagination


class RecruiterDetailView(DetailView):
    model = Recruiter
    template_name = "recruiters/recruiter_detail.html"  # replace with your template name
    context_object_name = "recruiter"


class RecruiterCreateView(CreateView):
    model = Recruiter
    form_class = RecruiterForm
    template_name = "recruiters/recruiter_create.html"
    success_url = "/recruiters/"  # replace with your URL


class RecruiterUpdateView(UpdateView):
    model = Recruiter
    fields = ["name", "company", "email", "phone"]
    template_name = "recruiters/recruiter_update.html"
    context_object_name = "recruiter"

    def get_success_url(self):
        return reverse("recruiter-detail", kwargs={"pk": self.object.pk})
