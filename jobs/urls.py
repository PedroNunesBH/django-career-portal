from django.urls import path
from jobs.views import (JobOffersList, CreateOfferView, EditOffer, DetailOffer, DeleteOffer, HomePage, MyOffers,
                        PopularOffers)

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('job_list/', JobOffersList.as_view(), name='job_list'),
    path('create_offer/', CreateOfferView.as_view(), name='create_offer'),
    path('update_offer/<int:pk>', EditOffer.as_view(), name='update_offer'),
    path('detail_offer/<int:pk>', DetailOffer.as_view(), name='detail_offer'),
    path('delete_offer/<int:pk>', DeleteOffer.as_view(), name='delete_offer'),
    path('my_offers/', MyOffers.as_view(), name='my_offers'),
    path('popular_offers/', PopularOffers.as_view(), name='popular_offers'),
]