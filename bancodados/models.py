from django.db import models

# Create your models here.
#tabelas do banco de dados 
#Transformando o codigo python em SQL
class Usuario(models.Model):
    #id    = models.AutoField(primary_key=True)
    nome    = models.CharField(max_length=50)
    idade   = models.IntegerField()
    email   = models.EmailField(max_length=100)
    password= models.CharField(max_length=20)
    def __str__ (self):
        return self.nome
    def __int__ (self):
       return self.idade
    def __int__ (self):
        return self.email
    def __int__ (self):
        return self.password

class Produto(models.Model):
    #id    = models.AutoField(primary_key=True)
    nome         = models.CharField(max_length=50)
    quantidade   = models.IntegerField()
    descricao    = models.TextField(max_length=50,blank=True)
    preco        = models.FloatField(null=True)
    categoria    = models.CharField(max_length=20,blank=True)
    tipo         = models.CharField(max_length=10,null=True)


    def __str__(self):
        return self.nome
    def __int__(self):
        return self.quantidade
    def __str__(self):
        return self.descricao
    def __flot__(self):
        return self.preco
    def __str__(self):
        return self.categoria
    def __str__(self):
        return self.tipo