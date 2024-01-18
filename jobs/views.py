from django.shortcuts import render
from django.views.generic import ListView
from .models import JobOffer


class JobOffersList(ListView):
    template_name = 'job_list.html'
    model = JobOffer
