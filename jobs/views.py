from django.shortcuts import redirect
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import JobOffer
from .forms import CreateOfferJob


class HomePage(TemplateView):
    template_name = 'homepage.html'


class JobOffersList(ListView):
    template_name = 'job_list.html'
    model = JobOffer

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        queryset = queryset.filter((Q(title__icontains=search) |
                                    Q(offer_requirements__icontains=search)) & Q(allowed=1))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["search"] = self.request.GET.get("search", "")
        print(self.request.GET)
        return context


@method_decorator(login_required(), name='dispatch')  # Permite que apenas usuarios logados acessem a view
class CreateOfferView(CreateView):
    template_name = 'create_offer.html'
    model = JobOffer
    form_class = CreateOfferJob
    success_url = reverse_lazy('my_offers')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user  # Preenche o campo autor do form com o username do usuario
        form.instance.recruiter_email = self.request.user.email  # Preenche o campo com o email do usuario
        return super().form_valid(form)


@method_decorator(login_required(), name='dispatch')  # Permite que apenas usuarios logados acessem a view
class EditOffer(UpdateView):
    template_name = 'update_offer.html'
    model = JobOffer
    form_class = CreateOfferJob
    success_url = reverse_lazy('my_offers')

    def get(self, request, *args, **kwargs):
        offer = self.get_object()  # Captura o objeto
        user_session = self.request.user
        offer_user = offer.autor
        if user_session == offer_user:
            return super().get(request, *args, **kwargs)
        else:
            return redirect('job_list')


class DetailOffer(DetailView):
    template_name = 'detail_offer.html'
    model = JobOffer

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['offer'] = context['object']
        return context

    def get(self, request, *args, **kwargs):
        offer = self.get_object()  # Capturando a offer da request
        offer.number_of_views += 1  # Adiciona em number_of_views da offer 1 a cada get
        offer.save()  # Salva no model
        return super().get(request, *args, **kwargs)


@method_decorator(login_required(), name='dispatch')  # Permite que apenas usuarios logados acessem a view
class DeleteOffer(DeleteView):
    template_name = 'delete_offer.html'
    model = JobOffer
    success_url = reverse_lazy('job_list')

    def get(self, request, *args, **kwargs):
        offer = self.get_object()  # Captura o objeto a ser excluido
        user_session = self.request.user  # Verifica o usuario que esta fazendo a requisicao
        offer_user = offer.autor  # Verifica o campo autor do objeto a ser excluido
        if user_session == offer_user:  # verifica se o usuario da requisicao é o mesmo que criou o objeto
            return super().get(request, *args, **kwargs)
        else:
            return redirect('job_list')


@method_decorator(login_required(), name='dispatch')  # Permite que apenas usuarios logados acessem a view
class MyOffers(ListView):
    template_name = 'my_offers.html'
    model = JobOffer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.user.id
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(autor_id=user_id, title__icontains=search, allowed=1)  # Filtra os anuncios do usuario E que o titulo contem search
            return queryset
        queryset = queryset.filter(autor_id=user_id, allowed=1)
        return queryset


class PopularOffers(ListView):
    template_name = 'popular_offers.html'
    model = JobOffer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = JobOffer.objects.filter(allowed=1).order_by('number_of_views')[0:10]  # Captura as 10 offers mais visualizadas
        return queryset