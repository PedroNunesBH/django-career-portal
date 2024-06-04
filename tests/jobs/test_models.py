from django.core.exceptions import ValidationError
from django.utils import timezone
from parameterized import parameterized
from ..test_class_base import TestBase
from jobs.models import JobOffer
from jobs.models import JobListingCount


class TestMaxLengthFieldsValidation(TestBase):
    def setUp(self):
        self.job_offer = self.create_object_job_offer()
        return super().setUp()

    @parameterized.expand([
        ("title", 100),
        ("organization_name", 100),
        ("location", 100),
        ("offer_requirements", 300),
        ("employment_type", 100),
    ])
    def test_max_length_of_fields(self, field_name, max_length):
        setattr(self.job_offer, field_name, "A" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.job_offer.full_clean()


class TestDefaultField(TestBase):
    def test_number_of_views_field_default_value(self):
        self.offer = self.create_object_job_offer()
        numbers_of_view_default = JobOffer._meta.get_field("number_of_views").default  # Acessa o valor default do campo
        self.assertEqual(numbers_of_view_default, 0)


class TestJobOfferStrRepresentation(TestBase):
    def test_job_offer_model_str_representation(self):
        self.offer = self.create_object_job_offer()
        offer_name = JobOffer.objects.get(pk=self.offer.pk).title  # Captura o titulo da joboffer criada/1a
        self.assertEqual(str(self.offer), offer_name)


class TestJobListingCountModel(TestBase):
    def test_job_listing_count_model_str_representation(self):
        self.job_listing_count = JobListingCount.objects.create(date_and_time=timezone.now(),
                                                                number_of_offers=1)
        number_of_offers = JobListingCount.objects.all().count()  # Captura o numero total de ofertas
        self.assertEqual(str(self.job_listing_count), str(number_of_offers))
