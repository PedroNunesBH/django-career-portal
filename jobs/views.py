from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import JobOffer
from .forms import CreateOfferJob
from django.urls import reverse_lazy


class JobOffersList(ListView):
    template_name = 'job_list.html'
    model = JobOffer

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('query')
        if search:
            queryset = queryset.filter(title__icontains=search)
            return queryset
        return queryset


class CreateOfferView(CreateView):
    template_name = 'create_offer.html'
    model = JobOffer
    form_class = CreateOfferJob
    success_url = reverse_lazy('job_list')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
