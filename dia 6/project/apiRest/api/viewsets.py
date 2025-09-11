from rest_framework import viewsets
from apiRest.api.serializers import EnderecoSerializer
from apiRest.models import Endereco
import requests

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def perform_create(self, serializer):
        cep = serializer.validated_data['cep']
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

        if response.status_code == 200:
            response.raise_for_status()
            data = response.json()
            serializer.save(
                logradouro=data.get('logradouro', ''),
                bairro=data.get('bairro', ''),
                localidade=data.get('localidade', ''),
                uf=data.get('uf', ''),
                cep=data.get('cep', '')
            )
        else:
            serializer.save()

        return super().perform_create(serializer)