

from django.urls import path
from .views import home, cadastrar

urlpatterns = [
    path('', home, name='home'),  # Página inicial
    path('cadastro/', cadastrar, name='cadastro'),
]
