from django.urls import path 
from .views import * 
urlpatterns = [
    path("home" ,index , name="dashboard") , 
    path('forms',form , name="formclick"),
    path('table',table , name="tabel"),
    path("delete/<int:id>", delete , name="delete"), 
    path("edit/<int:id>", edit , name="edit"),
    
]
