from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.


def estoque_view(request):
    return JsonResponse({
        "estatus":"Pagina de estoque"})