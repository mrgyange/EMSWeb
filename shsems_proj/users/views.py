from django.shortcuts import render

from django.views.generic import CreateView

from django.urls import reverse_lazy

from .forms import ParticipantCreationForm

class SignUpView(CreateView):
    form_class = ParticipantCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
