from django.contrib import admin

from .models import Cliente, Funcionario, MateriaPrima, Pedido, Produto

admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(MateriaPrima)
admin.site.register(Pedido)
admin.site.register(Produto)
