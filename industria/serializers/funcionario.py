from rest_framework.serializers import ModelSerializer
from industria.models import Funcionario

class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = "__all__"