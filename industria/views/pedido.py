from rest_framework.viewsets import ModelViewSet
from industria.serializers import PedidoSerializer
from industria.models import Pedido

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer