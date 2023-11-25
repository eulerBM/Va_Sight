from django.db import models

class player_key(models.Model):
    player = models.CharField(max_length=50, verbose_name='Nome do jogador')
    key = models.CharField(max_length=100, verbose_name='Chave da mira')
    image = models.ImageField(blank=True, verbose_name='Imagem da mira', upload_to="static/img/")


    def __str__(self):
        return f"Mira de {self.player}"