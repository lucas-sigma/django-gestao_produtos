from django.urls import path
from .views import estoque, addProduto, addCodProduto, addCategoria
from .views import updateProduto, deleteProduto, modifyQtdProdutos

urlpatterns = [
    path('estoque/', estoque, name = 'estoque'),
    path('addProduto/', addProduto, name='add_produto'),
    path('addCodProduto/', addCodProduto, name='cod_produto_form'),
    path('addCategoria/', addCategoria, name='categoria_form'),
    path('updateProduto/<int:id>', updateProduto, name='update_produto'),
    path('deleteProduto/<int:id>', deleteProduto, name='delete_produto'),
    path('editQtdProdutos/<int:id>/<str:operacao>', modifyQtdProdutos, name='updProduto')
]