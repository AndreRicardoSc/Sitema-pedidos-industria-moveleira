from rest_framework.viewsets import ModelViewSet
from serializers import FuncionarioSerializer
from models import Funcionario

class FuncionarioViewSet(ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer