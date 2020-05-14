from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

from pets.models import Pet, Appointment


class PetTests(TestCase):
    def test_list(self):
        user = User.objects.create_user(username='usertest', password='testing123')
        self.client.login(username='usertest', password='testing123')

        pet = Pet.objects.create(pet_name='Emmy', species='Fish', breed='Puggy', weight_in_pounds=0.6, owner=user)
        pet.save()

        res = self.client.get(f'/pets/')

        self.assertEqual(res.status_code, 200)

        self.assertContains(res, 'Emmy')

        pet_object = Pet.objects.get(owner=user)
        self.assertEqual(pet_object.owner, user)

    def test_detail(self):
        user = User.objects.create_user(username='usertest', password='testing123')
        self.client.login(username='usertest', password='testing123')

        pet = Pet.objects.create(pet_name='Emmy', species='Fish', breed='Puggy', weight_in_pounds=0.6, owner=user)
        pet.save()

        appointment = Appointment.objects.create(date_of_appointment=timezone.now(), duration_minutes=30, special_instructions='dont scale', pet=pet)
        appointment.save()

        res = self.client.get(f'/pets/{pet.id}/')
        self.assertEqual(res.status_code, 200)

        pet_object = Pet.objects.get(pet_name='Emmy')
        self.assertEqual(pet_object.pet_name, 'Emmy')