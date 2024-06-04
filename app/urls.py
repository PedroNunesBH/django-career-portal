from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts.views import UserRegisterView, login_view, logoutview
from accounts.views import CustomizedPasswordResetView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logoutview, name='logout'),
    path('password_reset/', CustomizedPasswordResetView.as_view(), name='password_reset'),
    # Pagina para inserção do email do usuario que redireciona para password_reset_done
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    # Pagina que notifica o usuario que um email foi enviado
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='new_password_form.html'), name='password_reset_confirm'),
    # Pagina do link do email para colocar nova senha
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete_advice.html'), name='password_reset_complete'),
    path("", include("jobs.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
