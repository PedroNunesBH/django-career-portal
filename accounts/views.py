from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UpgradeUserCreationForm
from django.contrib.auth.views import PasswordResetView


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']  # Captura o valor de username
        password = request.POST['password']  # Captura o valor de password
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Realiza o login
            return redirect('my_offers')  # Redireciona o usuario para a pagina de name my_offers
        else:
            auth_form = AuthenticationForm(data=request.POST)
    else:
        auth_form = AuthenticationForm()
    return render(request, "login.html", {'auth_form': auth_form})


class UserRegisterView(CreateView):
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('login')
    form_class = UpgradeUserCreationForm


def logoutview(request):
    logout(request)
    return redirect('job_list')


class CustomizedPasswordResetView(PasswordResetView):
    template_name = 'password_reset_form.html'  # Define o template da pagina para inserir email para recuperação
    email_template_name = 'password_reset_email.html'  # Define o conteúdo do email
    subject_template_name = 'recovery_email_subject.txt'  # Define o assunto do email
