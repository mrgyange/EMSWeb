from django.shortcuts import render

from django.views.generic import CreateView, DetailView, TemplateView

from .models import Registration
from users.models import Participant
from events.models import Event

class JoinEventView(CreateView):
    model = Registration
    fields = ['parents_permit', 'parents_contact_number',
        'waiver']

    template_name = "join_event.html"

    def form_valid(self, form):
        form.instance.participant = self.request.user
        print(self.kwargs['event_pk'])
        qs = Event.objects.filter(pk= self.kwargs['event_pk'])
        
        form.instance.event =  qs.first()
        return super().form_valid(form)

class RegistrationDetailView(DetailView):
    model = Registration
    template_name = "registration_detail.html"
    context_object_name = "registration"

class RegistrationListView(TemplateView):
    
    template_name = "registration_list.html"
    

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**)
        qs = Registration.objects.all()
        data ["registration_list"] = qs
        return data

