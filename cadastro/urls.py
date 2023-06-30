from django.urls import path
from cadastro import views

urlpatterns = [
    path("",views.cadastro_views                ,name = "cadastro_views"),
    path("buscar/<id>",views.buscar_usuario_view,name = "buscar_usuario"),
    path("registro",views.registrar_usuario_view,name = "cadastro_usuario")
]