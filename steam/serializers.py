from rest_framework import serializers # Importa o módulo de serialização do Django REST Framework
from .models import Game # Importa o modelo Game definido na aplicação

class GameSerializer(serializers.ModelSerializer):
    # Serializador para o modelo Game
    class Meta:
        model = Game # Especifica o modelo a ser serializado
        fields = '__all__'  # Inclui todos os campos do modelo