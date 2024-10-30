from rest_framework import serializers
from .models import ContactUs

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message', 'created_at']