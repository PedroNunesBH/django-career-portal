from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UpgradeUserCreationForm


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']  # Captura o valor de username
        password = request.POST['password']  # Captura o valor de password
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Realiza o login
            return redirect('job_list')  # Redireciona o usuario para a pagina de name cars_list
        else:
            auth_form = AuthenticationForm(data=request.POST)
    else:
        auth_form = AuthenticationForm()
    return render(request, "login.html", {'auth_form': auth_form})


class UserRegisterView(CreateView):
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('job_list')
    form_class = UpgradeUserCreationForm


def logoutview(request):
    logout(request)
    return redirect('job_list')
