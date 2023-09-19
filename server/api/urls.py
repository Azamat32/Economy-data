from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('topics/', GetTopics.as_view()),
    path('economic_indices/<int:pk>/', GetEconomicIndices.as_view()), 
    path('economic_index/<int:pk>/', GetEconomicIndex.as_view()),    
    path('economic_index_excel/<int:pk>/', get_economic_index_excel),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),    
]