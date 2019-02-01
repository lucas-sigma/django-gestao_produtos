from django.urls import path
from .views import estoque

urlpatterns = [
    path('estoque/', estoque, name = 'estoque')
]