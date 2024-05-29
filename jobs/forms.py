from django.forms import ModelForm
from jobs.models import JobOffer


class CreateOfferJob(ModelForm):

    class Meta:
        model = JobOffer
        fields = ['title', 'description', 'organization_name', 'location', 'offer_requirements',
                  'employment_type', 'salary', 'organization_description']

        labels = {
            'title': 'Título',
            'description': 'Descrição',
            'organization_name': 'Nome da Empresa',
            'location': 'Localização',
            'offer_requirements': 'Requisitos da Oferta',
            'employment_type': 'Tipo de Emprego',
            'salary': 'Salário',
            'organization_description': 'Descrição da Organização'
        }
