from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import JobOffer
from .forms import CreateOfferJob
from django.urls import reverse_lazy


class JobOffersList(ListView):
    template_name = 'job_list.html'
    model = JobOffer


class CreateOfferView(CreateView):
    template_name = 'create_offer.html'
    model = JobOffer
    form_class = CreateOfferJob
    success_url = reverse_lazy('job_list')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
