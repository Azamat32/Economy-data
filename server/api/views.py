from rest_framework.views import APIView
from rest_framework import generics
from .models import Economic_index, Topic, Table
from .serializer import EconomicIndexSerializer, TopicSerializer
from django.http import FileResponse, JsonResponse
from django.http import Http404
#from rest_framework.response import Response
#from rest_framework import status
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
             tables = Table.objects.get(id=pk)
             excel_file_path = os.path.join('static', 'tables', tables.path + '.xlsx')  
             if os.path.isfile(excel_file_path):
                 excel_response = FileResponse(open(excel_file_path, 'rb'), as_attachment=True, filename=tables.path)
                 return excel_response
             else:
                 return JsonResponse({"error": "Excel file not found."}, status=404)
         except Economic_index.DoesNotExist:
             return JsonResponse({"error": "Economic index with the specified ID does not exist."}, status=404) 

# class SaveExcel(APIView):
#     def post(self, request, pk):
#         if request.FILES.get('excel_file'):
#             excel_file = request.FILES['excel_file']

#             # Путь к каталогу static/excel_files
#             excel_files_dir = os.path.join('static', 'Excel')

#             related_indices = Economic_index.objects.get(id=pk)
#             excel_file_path = os.path.join(excel_files_dir, related_indices.path)

#             # Проверить, существует ли каталог static/Excel
#             if not os.path.exists(excel_files_dir):
#                 os.makedirs(excel_files_dir)

#             # Удаляем старый файл, если он существует
#             if os.path.exists(excel_file_path):
#                 os.remove(excel_file_path)

#             # Сохранить Excel-файл в каталог static/Excel
#             with open(excel_file_path, 'wb') as destination:
#                 for chunk in excel_file.chunks():
#                     destination.write(chunk)

#             return Response({'message': 'Excel-файл успешно сохранен в каталоге static/Excel/'}, status=status.HTTP_201_CREATED)

#         return Response({'error': 'No Excel file provided.'}, status=status.HTTP_400_BAD_REQUEST)