from django.shortcuts import render
from django.http import HttpResponse
from .models import Endereco
from .forms import EnderecoForm
import requests

def home(request):
    return render(request, 'home.html')

def buscar_cep(request):
    form = EnderecoForm(request.GET or None) #Pega os dados do formulário
    endereco = None
    erro = None

    if form.is_valid():
        cep = form.cleaned_data['cep'] #Faz a limpeza dos dados
        try:
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

            if response.status_code == 200:
                data = response.json()

                if data.get("erro"):
                    return render(request, 'endereco.html', {'erro': data.get("erro")})
                else:
                    endereco = Endereco(
                        rua = data.get('logradouro', ''),
                        bairro = data.get('bairro', ''),
                        cidade = data.get('localidade', ''),
                        estado = data.get('uf', ''),
                        cep = data.get('cep', '')
                    )
                    endereco.save()

        except requests.exceptions.RequestException:
            erro = f"Erro ao buscar o CEP: {cep}"
            
    return render(request, 'endereco.html', {'endereco': endereco})