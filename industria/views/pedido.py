from rest_framework.viewsets import ModelViewSet
from industria.serializers import PedidoSerializer, PedidoDetailSerializer
from industria.models import Pedido

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    
    def get_serializer_class(self):
        if self.action == "list":
            return PedidoDetailSerializer
        else:
            return PedidoSerializer