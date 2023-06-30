from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
#from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

def login_view(request):
    if request.method == 'POST' or request.method == 'GET':
        username = request.POST.get('username') or request.GET.get('username')
        password = request.POST.get('password') or request.GET.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # O usuário existe e as credenciais estão corretas
            return JsonResponse({"status": "Login bem-sucedido"})
        else:
            # As credenciais estão incorretas ou o usuário não existe
            return JsonResponse({"status": "Credenciais inválidas"})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])