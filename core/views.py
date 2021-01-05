from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from core.forms import RegistrationForm


class HomeView(View):
    def get(self, request):
        return render(request, 'core/home.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'core/register.html')

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Registration successful!')
            return HttpResponseRedirect(reverse('core:login'))

        # Form has errors
        return render(request, 'core/register.html', {'form': form})