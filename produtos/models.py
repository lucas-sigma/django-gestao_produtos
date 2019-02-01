from django.db import models
from django.utils.crypto import get_random_string

class Produto(models.Model):
    codigoDoProduto  =  get_random_string(length=10)
    nomeDoProduto    =  models.CharField('Nome do Produto', max_length=32)
    #categoria        =  models
    estoqueMinimo    =  models.IntegerField('Estoque Mínimo')
    estoqueAtual     =  models.IntegerField('Estoque Atual')
    precoDoProduto   =  models.DecimalField('Preço', max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nomeDoProduto