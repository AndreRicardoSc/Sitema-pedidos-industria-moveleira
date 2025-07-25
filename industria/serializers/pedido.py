from rest_framework.serializers import ModelSerializer
from industria.models import Pedido

class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"

class PedidoDetailSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"
        depth = 1