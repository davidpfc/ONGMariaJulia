from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UsuarioForm


def home(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'home.html')

# def cadastros(request):
#     return render(request, 'cadastro.html')

def cadastros(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados do formulário no banco de dados
            return redirect('home')  # Redireciona para a página 'home' após o sucesso
    else:
        form = UsuarioForm()
    return render(request, 'cadastro.html', {'form': form})
