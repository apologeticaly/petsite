from . import views
from django.urls import path
from pets.views import HomeView, PetCreateView, PetsListView, PetDetailView, CalendarListView, AppointmentCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home-page'),
    path('pets/', PetsListView.as_view(), name='pets-list-page'),
    path('pet/create/', PetCreateView.as_view(), name='pet-create-page'),
    path('pets/<int:pet_id>/', PetDetailView.as_view(), name='pet-detail-page'),
    path('calendar/', CalendarListView.as_view(), name='calendar-list-page'),
    path('appointment/create/', AppointmentCreateView.as_view(),
         name='appointment-create-page'),
]
