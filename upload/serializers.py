from django.db.models import fields
from rest_framework import serializers
from .models import Upload

#Created modelSerializer for each user

class UploadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'