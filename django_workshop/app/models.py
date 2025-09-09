from django.db import models

class pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome