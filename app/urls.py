"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jobs.views import (JobOffersList, CreateOfferView, EditOffer, DetailOffer, DeleteOffer, HomePage, MyOffers,
                        PopularOffers)
from accounts.views import UserRegisterView, login_view, logoutview
from django.contrib.auth import views as auth_views
from accounts.views import CustomizedPasswordResetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='homepage'),
    path('job_list/', JobOffersList.as_view(), name='job_list'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('create_offer/', CreateOfferView.as_view(), name='create_offer'),
    path('logout/', logoutview, name='logout'),
    path('update_offer/<int:pk>', EditOffer.as_view(), name='update_offer'),
    path('detail_offer/<int:pk>', DetailOffer.as_view(), name='detail_offer'),
    path('delete_offer/<int:pk>', DeleteOffer.as_view(), name='delete_offer'),
    path('my_offers/', MyOffers.as_view(), name='my_offers'),
    path('popular_offers/', PopularOffers.as_view(), name='popular_offers'),
    path('password_reset/', CustomizedPasswordResetView.as_view(), name='password_reset'),
    # Pagina para inserção do email do usuario que redireciona para password_reset_done
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    # Pagina que notifica o usuario que um email foi enviado
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='new_password_form.html'), name='password_reset_confirm'),
    # Pagina do link do email para colocar nova senha
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete_advice.html'), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
