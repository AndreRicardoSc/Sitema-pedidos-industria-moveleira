from rest_framework.viewsets import ModelViewSet
from serializers import ClienteSerializer
from models import Cliente

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer