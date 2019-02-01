from django.shortcuts import render
from django.db.models import Sum
from .models import Produto
from decimal import Decimal

def estoque(request):
    produtos = {}
    produtos['produtos']    =  Produto.objects.all()
    produtos['valorTotal']  =  Produto.objects.aggregate(Sum('precoDoProduto'))
    produtos['valorTotal']  =  round(Decimal(produtos['valorTotal']['precoDoProduto__sum']), 2)
    produtos['statusEstoque'] = 0

    for produto in produtos['produtos']:
        if produto.estoqueAtual < produto.estoqueMinimo:
            produtos['statusEstoque'] += 1

    if (len(produtos['produtos']) / 2) < produtos['statusEstoque']:
        produtos['statusEstoque'] = 'danger'
    elif (len(produtos['produtos']) / 2) == produtos['statusEstoque']:
        produtos['statusEstoque'] = 'caution'
    else:
        produtos['statusEstoque'] = 'fine'

    return render(request, 'estoque.html', {'produtos':produtos})