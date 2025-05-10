from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario


def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'home.html')

def cadastros(request):
    return render(request, 'cadastro.html')

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.email = request.POST.get('email')

        novo_usuario.save()

    #pegar infos do banco
    usuarios={
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'listagem.html')
