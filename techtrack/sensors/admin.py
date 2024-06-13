from django.contrib import admin
from .models import Sensor, Data, Alert

admin.site.register(Sensor)
admin.site.register(Data)
admin.site.register(Alert)
