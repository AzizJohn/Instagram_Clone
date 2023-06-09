from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegisterForm

# Create your views here.


class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    fields = '__all__'




    # def get_success_url(self):
    #     return reverse_lazy('tasks')