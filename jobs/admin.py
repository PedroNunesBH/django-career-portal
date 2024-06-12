from django.contrib import admin
from .models import JobOffer


class JobOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'organization_name', 'location', 'publication_date', 'offer_requirements',
                    'employment_type', 'salary', 'organization_description', "company_site")
    search_fields = ('title',)

    def get_readonly_fields(self, request, obj=...):
        if request.user.is_superuser:
            return []
        else:
            return ["allowed"]


admin.site.register(JobOffer, JobOfferAdmin)
