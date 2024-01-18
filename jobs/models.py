from django.db import models


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

    def __str__(self):
        return self.title
