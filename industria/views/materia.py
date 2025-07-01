from rest_framework.viewsets import ModelViewSet
from industria.serializers import MateriaPrimaSerializer
from industria.models import MateriaPrima

class MateriaPrimaViewSet(ModelViewSet):
    queryset = MateriaPrima.objects.all()
    serializer_class = MateriaPrimaSerializer