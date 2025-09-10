from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name = 'base'),
    path('buscarcep/', views.BuscarCepFormView.as_view(), name = 'buscarcep'),
    path('listar/', views.EnderecoListView.as_view(), name = 'listar'),
    path('detalhe/<int:pk>/', views.EnderecoDetailView.as_view(), name = 'detalhe'),
    path('delete/<int:pk>/', views.EnderecoDeleteView.as_view(), name = 'delete'),
]