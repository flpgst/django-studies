from django.db import models

# Create your models here.

class Aula(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateTimeField('data liberação')
    def __str__(self):
      return self.nome
