from django.urls import path
from . import views


urlpatterns = [
    path("",views.estoque_view, name= "estoque")
    
]