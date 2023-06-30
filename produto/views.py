from django.http import JsonResponse #importando a estrututa do Json
from django.core import serializers #Serializer--> transforma um dado do BD para outro tipo de dado
from bancodados.models import Produto #Importando a class do banco_de_dados
import json
# Create your views here.


def produto_view(request):
    return JsonResponse({
        "status":"Pagina de produto"})

#Funcao para converter dado do Usuario(banco_dados)para json
def parse_jason(query_serializer):
    resposta_json = [] #lista
    for nome in query_serializer:
        i = {
            "nome": nome['fields']['nome']
        }
        resposta_json.append(i)
    return resposta_json



def V_cadastro_produto(request):
    if (request.method == 'POST'):
        
        #decodificando o json para padrão PT-BR
        decode_json = request.body.decode('utf-8')
        cadastro_produto = json.loads(decode_json)
        #salvando diretamento no bando Usuarios
        banco = Produto( nome=cadastro_produto['nome'],
                        quantidade=cadastro_produto['quantidade'],
                        descricao=cadastro_produto['descricao'],
                        preco=cadastro_produto['preco'],
                        categoria=cadastro_produto['categoria'],
                        tipo=cadastro_produto['tipo'],
        )
        banco.save()
        #identificador = parse_jason(Usuario.pk)        
        #retorno da request
        return JsonResponse({
            "status": "Cadastro realizado com sucesso",
    
            "informações_registro": {
                #"id":id,
                "nome":cadastro_produto['nome'],
                "quantidade":cadastro_produto['quantidade'],       
                "descricao":cadastro_produto['descricao'],       
                "preco":cadastro_produto['preco'],       
                "categoria":cadastro_produto['categoria'],       
                "tipo":cadastro_produto['tipo'],       
        }})
    