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
from jobs.views import JobOffersList, CreateOfferView, EditOffer
from accounts.views import UserRegisterView, login_view, logoutview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('job_list/', JobOffersList.as_view(), name='job_list'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('create_offer/', CreateOfferView.as_view(), name='create_offer'),
    path('logout/', logoutview, name='logout'),
    path('update_offer/<int:pk>', EditOffer.as_view(), name='update_offer'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
