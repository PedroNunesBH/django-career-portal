from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from jobs.models import JobOffer


class TestBase(TestCase):
    def create_object_job_offer(self, title="Desenvolvedor Full Stack",
                                description="Descrição da vaga de desenvolvedor Full Stack.",
                                organization_name="Empresa ABC",
                                location="Cidade XYZ",
                                publication_date=timezone.now(),  # Usando a hora atual
                                offer_requirements="Requisitos da vaga.",
                                employment_type="Tempo Integral",
                                salary=8.000,
                                organization_description="Descrição da organização.",
                                autor=None,
                                recruiter_email="recruiter@example.com",
                                number_of_views=0,
                                allowed=0):

        if autor is None:
            autor = User.objects.create_superuser(username='testuser', email='test@example.com', password='testpassword')

        job_offer = JobOffer.objects.create(title=title, description=description, organization_name=organization_name,
                                       location=location, publication_date=publication_date,
                                       offer_requirements=offer_requirements, employment_type=employment_type, organization_description=organization_description, autor=autor,
                                       recruiter_email=autor.email, allowed=allowed)

        return job_offer

    def create_test_user(self, username="teste", password="teste"):
        return User.objects.create_superuser(username=username, password=password)
