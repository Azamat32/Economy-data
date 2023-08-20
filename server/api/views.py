from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import GDP
from .serializer import GDPSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    result = GDP.objects.all()[:10]
    serializer = GDPSerializer(result, many = True)
    
    return Response(serializer.data)

