from rest_framework import serializers
from .models import Electro


class ElectroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electro
        fields = ('id', 'owner', 'elctronic_name', 'elctronic_image', 'description', 'created_at', 'updated_at')