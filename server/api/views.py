from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EconomicIndex
from .serializer import  EconomicIndexSerializer

@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        content_names = EconomicIndex.objects.select_related('macro').all()
        serializer = EconomicIndexSerializer(content_names, many=True)
        return Response(serializer.data)
    