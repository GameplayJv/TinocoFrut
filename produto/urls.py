from django.urls import path
from . import views

urlpatterns = [
    path("",                views.produto_view,      name= "produto_views"),
    path("cadastroProduto/",views.V_cadastro_produto, name= "produto_views"),
]