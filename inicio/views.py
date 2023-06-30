from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def inicio_views(request):
    return JsonResponse({
            "status": "Bem vindo na API - TinocoFrut"
    })