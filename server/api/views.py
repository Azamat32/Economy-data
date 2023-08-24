from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import GDP, ContentName, IndicatorsName
from .serializer import GDPSerializer, ContentNameSerializer, IndicatorsNameSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    result = GDP.objects.all()[:10]
    serializer = GDPSerializer(result, many = True)
    
    return Response(serializer.data)

@api_view(['GET'])
def hierarchical_data_view(request):
    if request.method == 'GET':
        content_names = IndicatorsName.objects.select_related('macro_id').all()
        serializer = IndicatorsNameSerializer(content_names, many=True)
        return Response(serializer.data)