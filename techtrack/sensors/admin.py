from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Sensor, Data, Alert

# Register your models here.
admin.site.register(Sensor)
admin.site.register(Data)
admin.site.register(Alert)
