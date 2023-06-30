from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio_views, name= "inico_views")
]