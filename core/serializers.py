from django.core import serializers
from rest_framework import serializers

from core.models import *



class ArquivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArquivoHash
        fields = "__all__"

