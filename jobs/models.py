from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class JobOffer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    organization_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now_add=True)  # Adicionará automaticamente a data e hora ao campo
    offer_requirements = models.CharField(max_length=300)
    employment_type = models.CharField(max_length=100)
    salary = models.FloatField(blank=True, null=True)  # define que por padrão o campo é não informado
    organization_description = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='car_user', editable=False, default=1)
    recruiter_email = models.EmailField(editable=False)
    number_of_views = models.IntegerField(default=0, editable=False)
    allowed = models.BooleanField(default=0)  # Controle de permissao para as vagas

    def __str__(self):
        return self.title


class JobListingCount(models.Model):
    date_and_time = models.DateTimeField(default=timezone.now)  # Define como padrao a data e horario do momento
    number_of_offers = models.IntegerField()

    def __str__(self):
        return str(self.number_of_offers)
