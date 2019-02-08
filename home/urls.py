from django.urls import path
from .views import home, my_logout, signup

urlpatterns = [
    path('', home, name = 'home'),
    path('signup/', signup, name = 'signup'),
    path('logout/', my_logout, name = 'my_logout')
]