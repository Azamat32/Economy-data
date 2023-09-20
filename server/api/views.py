from rest_framework.views import APIView
from rest_framework import generics
from .models import Economic_index, Topic
from .serializer import EconomicIndexSerializer, TopicSerializer
from django.http import FileResponse, JsonResponse
from django.http import Http404
import os



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

class GetEconomicIndex(generics.RetrieveUpdateDestroyAPIView):
    queryset = Economic_index.objects.all()
    serializer_class = EconomicIndexSerializer

class GetEconomicIndexExcel(APIView):
    def get(self, request, pk):
        try:
            related_indices = Economic_index.objects.get(id=pk)
            excel_file_path = os.path.join('static', 'Excel', related_indices.path)
            if os.path.isfile(excel_file_path):
                excel_response = FileResponse(open(excel_file_path, 'rb'), as_attachment=True, filename=related_indices.path)
                return excel_response
            else:
                return JsonResponse({"error": "Excel file not found."}, status=404)
        except Economic_index.DoesNotExist:
            return JsonResponse({"error": "Economic index with the specified ID does not exist."}, status=404)  