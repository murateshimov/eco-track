from django.db import models


class Sensor(models.Model):
    SENSOR_STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Maintenance')
    ]
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    installation_date = models.DateField()
    status = models.CharField(max_length=50, choices=SENSOR_STATUS_CHOICES)

    def __str__(self):
        return f"{self.model} - {self.type}"


class Data(models.Model):
    sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='data')
    timestamp = models.DateTimeField(auto_now_add=True)
    pm25 = models.FloatField()
    pm10 = models.FloatField()
    co2 = models.FloatField()

    def __str__(self):
        return f"Data from {self.sensor.model} on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"


class Alert(models.Model):
    sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='alerts')
    description = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Alert for {self.sensor.model} on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
