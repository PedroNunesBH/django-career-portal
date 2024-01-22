from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import JobOffer, JobListingCount


@receiver([post_save, post_delete], sender=JobOffer)  # Captura a exclusao/inclusao de um objeto no model JobOffer
def job_count_add(sender, instance, **kwargs):
    if kwargs.get('created', True) or kwargs.get('signal') == post_delete:  # Verifica se é uma exclusao ou criacao
        total_offers = JobOffer.objects.all().count()  # Retorna a contagem de todos os registros de JobOffer
        JobListingCount.objects.create(number_of_offers=total_offers)  # Cria um registro no model JobListing
    else:
        pass
