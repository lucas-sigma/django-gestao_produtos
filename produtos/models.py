from django.db import models

class CodigoProduto(models.Model):
    cod = models.CharField(max_length=10)

    def __str__(self):
        return self.cod.upper()

class Categoria(models.Model):
    tagProduto = models.CharField(max_length=32)

    def __str__(self):
        return self.tagProduto

class Produto(models.Model):
    codigoDoProduto  =  models.OneToOneField(CodigoProduto, on_delete=models.CASCADE)
    nomeDoProduto    =  models.CharField('Nome do Produto', max_length=32)
    # categoria        =  models.OneToOneField(Categoria, on_delete=models.CASCADE)
    categoria        =  models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estoqueMinimo    =  models.IntegerField('Estoque Mínimo')
    qtdProdutos      =  models.IntegerField('Quantidade de Produtos')
    precoDoProduto   =  models.DecimalField('Preço', max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nomeDoProduto