from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


class UserRegister(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/job_list'
