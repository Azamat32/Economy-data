from rest_framework import serializers
from .models import Topic, EconomicIndex

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class EconomicIndexSerializer(serializers.ModelSerializer):
    macro = TopicSerializer() 
    class Meta:
        model = EconomicIndex
        fields = '__all__'

class EconomicIndicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicIndex
        fields = '__all__' 



