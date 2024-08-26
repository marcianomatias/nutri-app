

from django import views
from django.urls import path, include

urlpatterns = [

    path('auth/', include('autenticacao.urls')),
    
]
