from django.urls import path
from .views import contato
#klsjd

urlpatterns = [
    path('contato/', contato, name="contato"),
]
