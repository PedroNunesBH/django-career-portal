from django.db import models
from django.contrib.auth.models import User


class JobOffer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    organization_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    publication_date = models.DateTimeField(auto_now_add=True)  # Adicionará automaticamente a data e hora ao campo
    offer_requirements = models.CharField(max_length=300)
    employment_type = models.CharField(max_length=100)
    salary = models.FloatField(default="Não informado")  # define que por padrão o campo é não informado
    organization_description = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='car_user', editable=False, default=1)
    recruiter_email = models.EmailField(editable=False)
    number_of_views = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.title
