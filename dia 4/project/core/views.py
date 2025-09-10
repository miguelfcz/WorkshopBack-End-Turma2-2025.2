from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Endereco
from .forms import EnderecoForm
from django.views.generic import FormView, ListView, DetailView, DeleteView
import requests

def base(request):
    return render(request, 'base.html')
#FormView de via cep
class BuscarCepFormView(FormView):
    template_name = 'enderecoFormView.html'
    form_class = EnderecoForm
    success_url = 'buscarcep/'

    def form_valid(self,form):
        cep = form.cleaned_data['cep']

        try:
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            response.raise_for_status()
            data = response.json()

            if data.get("erro"):
                form.add_error('cep', 'CEP não encontrado.')
                return self.form_invalid(form)
            else:
                endereco = Endereco(
                    rua=data.get('logradouro', ''),
                    bairro=data.get('bairro', ''),
                    cidade=data.get('localidade', ''),
                    estado=data.get('uf', ''),
                    cep=data.get('cep', '')
                )
                endereco.save()

        except requests.exceptions.RequestException:
            form.add_error('cep', 'Erro ao buscar o CEP.')
            return self.form_invalid(form)

        return render(self.request, self.template_name, {'form': form, 'endereco': endereco})

class EnderecoListView(ListView):
    model = Endereco
    template_name = 'enderecoListView.html'
    context_object_name = 'enderecos'

class EnderecoDetailView(DetailView):
    model = Endereco
    template_name = 'enderecoDetailView.html'
    context_object_name = 'endereco'

class EnderecoDeleteView(DeleteView):
    model = Endereco
    template_name = 'enderecoDeleteView.html'
    success_url = reverse_lazy('listar')