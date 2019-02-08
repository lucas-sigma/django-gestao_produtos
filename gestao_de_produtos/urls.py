from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from home import urls as home_urls
from produtos import urls as produtos_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('produtos/', include(produtos_urls)),
    path('login/', auth_views.LoginView.as_view(), name='login')
]
