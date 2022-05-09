from dataclasses import fields
from rest_framework import serializers
from django.db import models
from .models import stu
class StuSerializer(serializers.ModelSerializer):
    class meta:
        model = stu
        fields = '__all__'