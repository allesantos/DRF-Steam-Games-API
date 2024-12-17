from django.db import models

class Game(models.Model):
    steam_id = models.CharField(max_length=20)  # Steam ID do usuário
    appid = models.IntegerField()              # ID único do jogo na Steam
    name = models.CharField(max_length=255)    # Nome do jogo
    tempo_jogado = models.IntegerField()   # Tempo total jogado (em minutos)
    img_icon_url = models.CharField(max_length=255, null=True, blank=True)  # URL do ícone do jogo

    class Meta:
        unique_together = ('steam_id', 'appid')  # Evita duplicados por usuário e jogo

    def __str__(self):
        return self.name

