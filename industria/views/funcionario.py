from rest_framework.viewsets import ModelViewSet
from industria.serializers import FuncionarioSerializer
from industria.models import Funcionario

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer