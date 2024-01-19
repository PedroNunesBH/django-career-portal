from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import JobOffer
from .forms import CreateOfferJob
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class JobOffersList(ListView):
    template_name = 'job_list.html'
    model = JobOffer

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        queryset = queryset.filter(title__icontains=search)
        return queryset


@method_decorator(login_required(), name='dispatch')
class CreateOfferView(CreateView):
    template_name = 'create_offer.html'
    model = JobOffer
    form_class = CreateOfferJob
    success_url = reverse_lazy('job_list')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class EditOffer(UpdateView):
    template_name = 'update_offer.html'
    model = JobOffer
    form_class = CreateOfferJob
    success_url = reverse_lazy('job_list')


class DetailOffer(DetailView):
    template_name = 'detail_offer.html'
    model = JobOffer

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['offer'] = context['object']
        return context
