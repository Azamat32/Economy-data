from rest_framework import serializers
from .models import Topic, Economic_index

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class EconomicIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Economic_index
        fields = '__all__'




