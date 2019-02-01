from django.urls import path
from .views import home, logout, signup

urlpatterns = [
    path('', home, name = 'home'),
    path('signup/', signup, name = 'signup'),
    path('logout/', logout, name = 'logout')
]