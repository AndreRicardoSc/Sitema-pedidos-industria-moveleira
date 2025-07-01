from rest_framework.viewsets import ModelViewSet
from industria.serializers import ProdutoSerializer, ProdutoDetailSerializer
from industria.models import Produto

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoDetailSerializer
        else:
            return ProdutoSerializer
