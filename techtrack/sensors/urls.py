from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Creating a router to automatically manage URL routing for viewsets
router = DefaultRouter()
router.register(r'sensors', views.SensorViewSet)
router.register(r'data', views.DataViewSet)
router.register(r'alerts', views.AlertViewSet)

# Include the router paths and any specific paths if necessary
urlpatterns = [
    path('', include(router.urls)),
]
