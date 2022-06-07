import imp
from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet

router = DefaultRouter()

router.register('api',ContactViewSet)

urlpatterns = [

    path('', include(router.urls))
]