from django.urls import include, path
from .views import (
    home,

    lista_pessoas,
    nova_pessoa,
    update_pessoa,
    delete_pessoa,
    
    lista_veiculos,
    novo_veiculo,
    update_veiculo,
    delete_veiculo,
    
    lista_movRotativos,
    novo_movRotativo,
    update_movRotativo,
    delete_movRotativo,
    
    lista_mensalistas,
    novo_mensalista,
    update_mensalista,
    delete_mensalista,
    
    lista_movMensalista,
    novo_movMensalista,
    update_movMensalista,
    delete_movMensalista,
)

urlpatterns = [
    path('', home, name='core_home'),
    
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('nova-pessoa/', nova_pessoa, name='core_nova_pessoa'),
    path('update-pessoa/<int:id>', update_pessoa, name='core_update_pessoa'),
    path('delete-pessoa/<int:id>', delete_pessoa, name='core_delete_pessoa'),
    
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('novo-veiculo/', novo_veiculo, name='core_novo_veiculo'),
    path('update-veiculo/<int:id>', update_veiculo, name='core_update_veiculo'),
    path('delete-veiculo/<int:id>', delete_veiculo, name='core_delete_veiculo'),
    
    path('movimento-rotativo/', lista_movRotativos, name='core_lista_movRotativos'),
    path('novo-movimento-rotativo/', novo_movRotativo, name='core_novo_movRotativo'),
    path('update-movimento-rotativo/<int:id>', update_movRotativo, name='core_update_movRotativo'),
    path('delete-movimento-rotativo/<int:id>', delete_movRotativo, name='core_delete_movRotativo'),
    
    path('mensalistas/', lista_mensalistas, name='core_lista_mensalistas'),
    path('novo-mensalista/', novo_mensalista, name='core_novo_mensalista'),
    path('update-mensalista/<int:id>', update_mensalista, name='core_update_mensalista'),
    path('delete-mensalista/<int:id>', delete_mensalista, name='core_delete_mensalista'),
    
    path('movimento-mensalista/', lista_movMensalista, name='core_lista_movMensalista'),
    path('novo-movimento-mensalista/', novo_movMensalista, name='core_novo_movMensalista'),
    path('update-movimento-mensalista/<int:id>', update_movMensalista, name='core_update_movMensalista'),
    path('delete-movimento-mensalista/<int:id>', delete_movMensalista, name='core_delete_movMensalista'),
]
