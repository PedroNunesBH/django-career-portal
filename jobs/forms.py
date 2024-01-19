from django.forms import ModelForm
from jobs.models import JobOffer


class CreateOfferJob(ModelForm):

    class Meta:
        model = JobOffer
        fields = "__all__"
