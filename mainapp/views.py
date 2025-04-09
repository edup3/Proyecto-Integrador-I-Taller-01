from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, CreateView, TemplateView
from .forms import *
from django.urls import reverse


# Create your views here.


class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        return redirect(reverse('home'))


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    model = User
    form_class = UserRegistrationForm

    def get_success_url(self):
        return redirect(reverse('register_done'))


class RegisterSuccess(TemplateView):
    template_name = 'registration/register_done.html'
