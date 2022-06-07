from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerialzer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerialzer
    