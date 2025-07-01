from rest_framework.viewsets import ModelViewSet
from serializers import MateriaPrimaSerializer
from models import MateriaPrima

class MateriaPrimaViewSet(ModelViewSet):
    queryset = MateriaPrima.objects.all()
    serializer_class = MateriaPrimaSerializer