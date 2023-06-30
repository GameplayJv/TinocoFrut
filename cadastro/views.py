from django.http import JsonResponse #importando a estrututa do Json
from django.core import serializers #Serializer--> transforma um dado do BD para outro tipo de dado
from bancodados.models import Usuario #Importando a class do banco_de_dados

import json

# Create your views here.

#Funcao para converter dado do Usuario(banco_dados)para json
def parse_jason(query_serializer):
    resposta_json = [] #lista
    for nome in query_serializer:
        i = {
            "nome": nome['fields']['nome']
        }
        resposta_json.append(i)
    return resposta_json
        


def registrar_usuario_view(request):
    if (request.method == 'POST'):
        
        #decodificando o json para padrão PT-BR
        decode_json = request.body.decode('utf-8')
        cadastro_usuario = json.loads(decode_json)
        #salvando diretamento no bando Usuarios
        banco = Usuario( nome=cadastro_usuario['nome'],
                        idade=cadastro_usuario['idade'],
                        email=cadastro_usuario['email'],
                        password=cadastro_usuario['password'])
        banco.save()
        
        #identificador = parse_jason(Usuario.pk)        
        #retorno da request
        return JsonResponse({
            "status": "Cadastro realizado com sucesso",
    
            "informações_registro": {
                #"id":id,
                "nome":cadastro_usuario['nome'],
                "email":cadastro_usuario['email']       
        }})
    
    elif (request.method=='GET'):
        query_set = Usuario.objects.all() #Buscando todas as request´s do BD
        query_serializer = serializers.serialize('json',query_set)
        nomes_jason = json.loads(query_serializer)
        resposta_json = parse_jason(nomes_jason)
        #retorno da request
        return JsonResponse(resposta_json,safe=False)
    
    elif(request.method == 'PUT'):
         #decodificando o json para padrão PT-BR
        decode_json = request.body.decode('utf-8')
        cadastro_usuario = json.loads(decode_json)
        buscar_request = Usuario.filter(pk=cadastro_usuario['id'])
        buscar_request.nome = cadastro_usuario['nome']
        buscar_request.save()
        
        return JsonResponse({
            "status": "Atualização feita",
    
            "Novo_Registro": {
                "id":buscar_request.pk,
                "nome":buscar_request.nome
                     
        }})




  


def cadastro_views(request):
    return JsonResponse({"identificador": 123,"nome": "Fravu","idade":22})


#Buscando um usuario por um identificador
def buscar_usuario_view(request, id):
    #Buscando um requerimento
    if (request.method == 'GET'):
        query_set = Usuario.objects.get(pk=id)
        query_serializer = json.loads(serializers.serialize('json',[query_set]))
        resposta_json = parse_jason(query_serializer)
        return JsonResponse(resposta_json,safe=False)
    
    
    
    
