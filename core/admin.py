from django.contrib import admin
from .models import (
    Marca,
    Veiculo,
    Pessoa,
    Parametros,
    MovimentoRotativo,
    Mensalista,
    MovimentoMensalista
)


class MovimentoRotativoAdmin(admin.ModelAdmin):
    list_display = (
        'veiculo',
        'checkin', 'checkout',
        'valor_hora', 'pago',
        'horas_total', 'total'
    )


class MensalistaAdmin(admin.ModelAdmin):
    list_display = (
        'veiculo',
        'inicio'
    )


class ParametrosAdmin(admin.ModelAdmin):
    list_display = ('id', 'valor_hora', 'valor_mes')


class MovimentoMensalistaAdmin(admin.ModelAdmin):
    list_display = (
        'mensalista',
        'data_pagamento',
        'total'
    )

# Register your models here.
admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros, ParametrosAdmin)
admin.site.register(MovimentoRotativo, MovimentoRotativoAdmin)
admin.site.register(Mensalista, MensalistaAdmin)
admin.site.register(MovimentoMensalista, MovimentoMensalistaAdmin)