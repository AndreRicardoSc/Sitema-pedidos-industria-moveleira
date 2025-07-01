from rest_framework.viewsets import ModelViewSet
from industria.serializers import ClienteSerializer
from industria.models import Cliente

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer