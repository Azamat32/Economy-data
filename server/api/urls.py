from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = "index"),  
    path('hierarchical-data/', views.hierarchical_data_view, name='hierarchical-data'),  
]