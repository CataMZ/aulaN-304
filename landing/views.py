from django.shortcuts import render

# Create your views here.

def mostrar_index(request):
    nome = 'Katrina'
    lista_compras = ['arroz', 'feijão', 'chocolate']
    return render(request, 'index.html', {'item' : nome, 'lista' : lista_compras})