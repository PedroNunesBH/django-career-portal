from django.contrib import admin
from .models import JobOffer


class JobOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'organization_name', 'location', 'publication_date', 'offer_requirements', 'employment_type', 'salary', 'organization_description')
    search_fields = ('title',)


admin.site.register(JobOffer, JobOfferAdmin)
