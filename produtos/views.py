from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, F
from django.contrib.auth.decorators import login_required

from .models import Produto, CodigoProduto, Categoria
from decimal import Decimal
from .forms import ProdutoForm, CodigoProdutoForm, CategoriaForm

@login_required
def modifyQtdProdutos(request, id, operacao):
    if operacao == '+':
        updProduto = Produto.objects.get(id=id)
        updProduto.qtdProdutos += 1
        updProduto.save()
    elif operacao == '-':
        updProduto = Produto.objects.get(id=id)
        updProduto.qtdProdutos -= 1
        updProduto.save()
    else:
        pass

    return redirect('estoque')

@login_required
def estoque(request):
    produtos = {}
    produtos['produtos']       =  Produto.objects.all()
    produtos['valorTotal']     =  Produto.objects.aggregate(Sum('precoDoProduto'))
    produtos['valorTotal']     =  round(Decimal(produtos['valorTotal']['precoDoProduto__sum']), 2)
    produtos['statusEstoque']  =  0
    produtos['qtdTotal']       =  Produto.objects.aggregate(Sum('qtdProdutos'))
    produtos['qtdTotal']       = produtos['qtdTotal']['qtdProdutos__sum']

    # Flag to make a status
    for produto in produtos['produtos']:
        if produto.qtdProdutos < produto.estoqueMinimo:
            produtos['statusEstoque'] += 1

    # Generate flags to status emoji
    if (len(produtos['produtos']) / 2) < produtos['statusEstoque']:
        produtos['statusEstoque'] = 'danger'
    elif (len(produtos['produtos']) / 2) == produtos['statusEstoque']:
        produtos['statusEstoque'] = 'caution'
    else:
        produtos['statusEstoque'] = 'fine'

    return render(request, 'estoque.html', {'produtos':produtos})

@login_required
def addCategoria(request):
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('add_produto')

    return render(request, 'categoria_form.html', {'form':form})

@login_required
def addCodProduto(request):
    form = CodigoProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('add_produto')

    return render(request, 'cod_produto_form.html', {'form':form})

@login_required
def addProduto(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('estoque')

    return render(request, 'estoque_form.html', {'form':form})

@login_required
def updateProduto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form    = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('estoque')

    return render(request, 'estoque_form.html', {'form':form})

@login_required
def updateCategoriaProduto(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    form      = CategoriaForm(request.POST or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect('estoque')

    return render(request, 'categoria_form.html', {'form':form})

@login_required
def updateCodProduto(request, id):
    cod  = get_object_or_404(CodigoProduto, pk=id)
    form = CodigoProdutoForm(request.POST or None, instance=cod)

    if form.is_valid():
        form.save()
        return redirect('estoque')

    return render(request, 'cod_produto_form.html', {'form':form})

@login_required
def deleteProduto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()

    return redirect('estoque')

@login_required
def deleteCodProduto(request):
    codList = CodigoProduto.objects.all()
    # return render(request, 'list_cod_produto_delete.html', {'cod':codList})

    #cod  = get_object_or_404(CodigoProduto, pk=id)
    #cod.delete()

    #return redirect('estoque')

    # cod  = get_object_or_404(CodigoProduto, pk=id)
    
    # if request.method == 'POST':
    #     cod.delete()
    #     return redirect('estoque')

    # return render(request, 'cod_produto_form.html')

@login_required
def deleteCategoria(request, id):
    categoria = get_object_or_404(Categoria)

    if request.method == 'POST':
        categoria.delete()

    return redirect('estoque')