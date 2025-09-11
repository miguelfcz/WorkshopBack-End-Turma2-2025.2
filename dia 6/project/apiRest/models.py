from django.db import models

class Endereco(models.Model):
    logradouro = models.CharField(max_length = 100)
    bairro = models.CharField(max_length = 100)
    localidade = models.CharField(max_length = 100)
    uf = models.CharField(max_length = 100)
    cep = models.CharField(max_length = 20)

    def __str__(self):
        return f"Rua: {self.rua}, Bairro: {self.bairro}, Cidade: {self.cidade}, Estado: {self.estado}, CEP: {self.cep}"