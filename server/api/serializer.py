from rest_framework import serializers
from .models import GDP, Region, IndicatorsName, ContentName

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class GDPSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = GDP
        fields = '__all__'

class IndicatorsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicatorsName
        fields = ['id', 'name', 'link']

class ContentNameSerializer(serializers.ModelSerializer):
    indicators = IndicatorsNameSerializer(many=True, read_only=True)

    class Meta:
        model = ContentName
        fields = ['id', 'name', 'indicators']
