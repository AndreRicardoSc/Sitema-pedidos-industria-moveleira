from rest_framework.viewsets import ModelViewSet
from serializers import ProdutoSerializer
from models import Produto

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer