from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from pets.models import Pet, Appointment


class HomeView(ListView):
    def get(self, req):
        return render(req, 'home.html')


class PetCreateView(CreateView):
    model = Pet
    fields = ['pet_name', 'species', 'breed', 'weight_in_pounds', 'owner']
    template_name = 'pet/create.html'


class PetsListView(ListView):
    model = Pet
    def get(self, req):
        pets = self.get_queryset().all()
        return render(req, 'pet/list.html', {
            'pets': pets
        })


class PetDetailView(DetailView):
    def get(self, req, pet_id):
        return render(req, 'pet/detail.html', {
            'pet': Pet.objects.get(id=pet_id)
        })


class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['date_of_appointment',
              'duration_minutes', 'special_instructions', 'pet']
    template_name = 'calendar/create.html'


class CalendarListView(ListView):
    model = Appointment
    def get(self, req):
        appointments = self.get_queryset().all()
        return render(req, 'calendar/list.html', {
            'appointments': appointments.filter(
                # renders things greater than today's date
                date_of_appointment__gte=timezone.now()
                # Sorts by the soonest first. Put '-' in front of the first argument for greatest to least.
                # Example: '-date_of_appointment' === greatest to least order
            ).order_by('date_of_appointment', 'date_of_appointment')
        })
