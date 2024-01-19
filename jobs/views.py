from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import JobOffer
from .forms import CreateOfferJob


class JobOffersList(ListView):
    template_name = 'job_list.html'
    model = JobOffer


class CreateOfferView(CreateView):
    template_name = 'create_offer.html'
    model = JobOffer
    form_class = CreateOfferJob
    success_url = 'job_list'
