from .models import Business
from rest_framework import serializers




class BusinessSerializers(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'
        
