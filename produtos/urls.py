from django.urls import path
from .views import estoque, addProduto, addCodProduto, addCategoria
from .views import updateCategoriaProduto, updateCodProduto, updateProduto
from .views import deleteCategoria, deleteCodProduto, deleteProduto, modifyQtdProdutos

urlpatterns = [
    path('estoque/', estoque, name = 'estoque'),
    path('addProduto/', addProduto, name='add_produto'),
    path('addCodProduto/', addCodProduto, name='cod_produto_form'),
    path('addCategoria/', addCategoria, name='categoria_form'),
    path('updateProduto/<int:id>', updateProduto, name='update_produto'),
    path('updateCategoria/<int:id>', updateCategoriaProduto, name='update_categoria'),
    path('updateCodProduto/<int:id>', updateCodProduto, name='update_cod_produto'),
    path('deleteProduto/<int:id>', deleteProduto, name='delete_produto'),
    path('deleteCategoria/<int:id>', deleteCategoria, name='delete_categoria'),
    path('deleteCodProduto/<int:id>', deleteCodProduto, name='delete_cod_produto'),
    path('editQtdProdutos/<int:id>/<str:operacao>', modifyQtdProdutos, name='updProduto')
]