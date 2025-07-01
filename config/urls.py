from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from industria.views import ClienteViewSet, FuncionarioViewSet, MateriaPrimaViewSet, PedidoViewSet, ProdutoViewSet

router = DefaultRouter()
router.register(r"clientes", ClienteViewSet)
router.register(r"funcionarios", FuncionarioViewSet)
router.register(r"materias-primas", MateriaPrimaViewSet)
router.register(r"pedidos", PedidoViewSet)
router.register(r"produtos", ProdutoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
