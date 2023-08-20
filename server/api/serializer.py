from rest_framework import serializers
from .models import GDP, Region

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class GDPSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = GDP
        fields = '__all__'
