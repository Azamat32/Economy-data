from rest_framework import serializers
from .models import Topic, Economic_index, Table

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class EconomicIndexSerializer(serializers.ModelSerializer):
    tables = TableSerializer(many=True, read_only=True)
    class Meta:
        model = Economic_index
        fields = '__all__'




