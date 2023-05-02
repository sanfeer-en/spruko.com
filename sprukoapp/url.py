from django.urls import path 
from .views import  * 
urlpatterns = [
    path("home" ,index , name="dashboard") , 
    path('forms',formpage , name="formclick")
]
