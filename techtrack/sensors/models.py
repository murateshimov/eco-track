from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Sensor(models.Model):
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    installation_date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.model} - {self.type}"


class Data(models.Model):
    sensor = models.ForeignKey(
        Sensor, related_name='data', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    co2 = models.FloatField()

    def __str__(self):
        return f"Data from {self.sensor.model} on {self.timestamp}"


class Alert(models.Model):
    sensor = models.ForeignKey(
        Sensor, related_name='alerts', on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert for {self.sensor.model} at {self.timestamp}"
