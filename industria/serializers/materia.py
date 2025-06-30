from rest_framework.serializers import ModelSerializer
from models import MateriaPrima


class MateriaPrimaSerializer(ModelSerializer):
    class Meta:
        model = MateriaPrima
        fields = "__all__"