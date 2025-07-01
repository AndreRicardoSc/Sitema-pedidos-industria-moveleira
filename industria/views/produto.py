from rest_framework.viewsets import ModelViewSet
from industria.serializers import ProdutoSerializer
from industria.models import Produto

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer