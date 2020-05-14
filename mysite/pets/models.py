from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime


class Pet(models.Model):
    pet_name = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    weight_in_pounds = models.DecimalField(max_digits=5, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        # Returns back to the list page after a new pet is created
        return reverse('pets-list-page')

    def __str__(self):
        return self.pet_name


class Appointment(models.Model):
    date_of_appointment = models.DateField(default=datetime.now)
    duration_minutes = models.IntegerField()
    special_instructions = models.CharField(max_length=400)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def get_absolute_url(self):
        # Returns back to the list page after a new pet is created
        return reverse('calendar-list-page')

    def __str__(self):
        return self.pet.pet_name
