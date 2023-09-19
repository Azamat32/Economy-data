from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Economic_index, Topic
from .serializer import EconomicIndexSerializer, TopicSerializer
from django.http import FileResponse, JsonResponse
from django.http import Http404
import os
import json


class GetTopics(generics.ListAPIView):
    queryset = Topic.objects.all()  
    serializer_class = TopicSerializer  

class GetEconomicIndices(generics.ListAPIView):
    serializer_class = EconomicIndexSerializer

    def get_queryset(self):
        macro_id = self.kwargs['pk'] 
        try:
            macro = Topic.objects.get(id=macro_id)
        except Topic.DoesNotExist:
            raise Http404("Topic with the specified ID does not exist.")

        related_indices = Economic_index.objects.filter(macro_topic=macro)
        return related_indices

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


class GetEconomicIndex(generics.RetrieveUpdateDestroyAPIView):
    queryset = Economic_index.objects.all()
    serializer_class = EconomicIndexSerializer
