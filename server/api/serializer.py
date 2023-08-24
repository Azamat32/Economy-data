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


class ContentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentName
        fields = '__all__'

class IndicatorsNameSerializer(serializers.ModelSerializer):
    macro_id = ContentNameSerializer() 
    class Meta:
        model = IndicatorsName
        fields = '__all__'

