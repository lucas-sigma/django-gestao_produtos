from django.contrib import admin
from .models import Produto, CodigoProduto, Categoria

admin.site.register(Produto)
admin.site.register(CodigoProduto)
admin.site.register(Categoria)