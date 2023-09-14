import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Economic_index, Topic
from .serializer import  EconomicIndexSerializer, TopicSerializer
from django.http import FileResponse, JsonResponse
import json

@api_view(['GET'])
def get_topics(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
        
    return Response(serializer.data)

@api_view(['POST'])
def get_economic_indices(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            macro_id = data.get('id')
            if macro_id is not None:
                try:
                    macro = Topic.objects.get(id=macro_id)
                    related_indices = Economic_index.objects.filter(macro_topic=macro)
                    serializer = EconomicIndexSerializer(related_indices, many=True)
                    return Response(serializer.data)
                except Topic.DoesNotExist:
                    return JsonResponse({"error": "Topic with the specified ID does not exist."}, status=404)
            else:
                return JsonResponse({"error": "Macro ID parameter is missing."}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data in the request body."}, status=400)
    
    return JsonResponse({"error": "Invalid request method."}, status=405)

@api_view(['POST'])
def get_economic_index_excel(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            macro_id = data.get('id')
            if macro_id is not None:
                try:
                    related_indices = Economic_index.objects.get(id=macro_id)
                    name_excel = related_indices.path
                    
                    excel_file_path = os.path.join('static', 'Excel', name_excel)

                    if os.path.isfile(excel_file_path):
                        excel_response = FileResponse(open(excel_file_path, 'rb'), as_attachment=True, filename=name_excel)                        
                        return excel_response
                    else:
                        return JsonResponse({"error": "Excel file not found."}, status=404)
                except Economic_index.DoesNotExist:
                    return JsonResponse({"error": "Economic index with the specified ID does not exist."}, status=404)
            else:
                return JsonResponse({"error": "Macro ID parameter is missing."}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data in the request body."}, status=400)
    
    return JsonResponse({"error": "Invalid request method."}, status=405)  

@api_view(['POST'])
def get_economic_index(request):
     if request.method == 'POST':
         try:
             data = json.loads(request.body)
             macro_id = data.get('id')
             if macro_id is not None:
                 try:
                     related_indices = Economic_index.objects.get(id=macro_id)
                     serializer = EconomicIndexSerializer(related_indices, many=False)
                    
                     excel_file_path = os.path.join('static', 'Excel', 'test1.xlsx')
                     return Response(serializer.data)
                  
                 except Economic_index.DoesNotExist:
                     return JsonResponse({"error": "Economic index with the specified ID does not exist."}, status=404)
             else:
                 return JsonResponse({"error": "Macro ID parameter is missing."}, status=400)
         except json.JSONDecodeError:
             return JsonResponse({"error": "Invalid JSON data in the request body."}, status=400)
    
     return JsonResponse({"error": "Invalid request method."}, status=405)
   