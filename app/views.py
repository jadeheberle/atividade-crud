# views.py
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.shortcuts import redirect, get_object_or_404 # Adicionado Jade

from django.urls import reverse_lazy
from .models import Funcionario

class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = '__all__'
    template_name = "form_funcionario.html"
    success_url = reverse_lazy('lista_funcionarios')

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "lista_funcionarios.html"

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = '__all__'
    template_name = 'form_funcionario.html'
    success_url = reverse_lazy('lista_funcionarios')

class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = "lista_funcionario.html"
    context_object_name = "fun"

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "remover_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")
    
def toggle_ativo_funcionario(request, pk): # Adicionado Jade
    funcionario = get_object_or_404(Funcionario, pk=pk)
    funcionario.ativo = not funcionario.ativo  # alterna True/False
    funcionario.save()
    return redirect('lista_funcionarios')

