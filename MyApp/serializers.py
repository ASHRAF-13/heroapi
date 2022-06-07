from dataclasses import fields
from rest_framework import serializers
from .models import Contact

class ContactSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'