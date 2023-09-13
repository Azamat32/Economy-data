from django.urls import path, include
from . import views

urlpatterns = [
    path('topics', views.get_topics, name = "topics"), 
    path('economic_indices', views.get_economic_indices, name = "economic_indices"),
    path('economic_index', views.get_economic_index, name = "economic_index"),    
    path('economic_index/excel', views.get_excel, name = "economic_index"),    

]