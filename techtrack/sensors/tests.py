from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Sensor
from django.contrib.auth.models import User


class SensorTests(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        # Create a sensor
        Sensor.objects.create(type='PM2.5', model='Model A',
                              installation_date='2023-01-01', status='active')

    def test_create_sensor(self):
        """Ensure we can create a new sensor object."""
        url = reverse('sensor-list')
        data = {'type': 'CO2', 'model': 'Model B',
                'installation_date': '2023-01-02', 'status': 'active'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sensor.objects.count(), 2)

    def test_get_sensors(self):
        """Ensure we can retrieve a list of sensors."""
        url = reverse('sensor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_sensor(self):
        """Ensure we can update a sensor object."""
        sensor = Sensor.objects.first()
        url = reverse('sensor-detail', args=[sensor.id])
        data = {'status': 'inactive'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        sensor.refresh_from_db()
        self.assertEqual(sensor.status, 'inactive')

    def test_delete_sensor(self):
        """Ensure we can delete a sensor object."""
        sensor = Sensor.objects.first()
        url = reverse('sensor-detail', args=[sensor.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Sensor.objects.count(), 0)
