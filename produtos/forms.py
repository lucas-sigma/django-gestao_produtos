from django.forms import ModelForm
from .models import Categoria, CodigoProduto, Produto

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class CodigoProdutoForm(ModelForm):
    class Meta:
        model = CodigoProduto
        fields = '__all__'

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        # fields = ['codigoDoProduto', 'nomeDoProduto', 'categoria', 'estoqueMinimo', 'estoqueAtual', 'precoDoProduto']
        fields = '__all__'