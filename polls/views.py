from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario


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

def doadores(request):
    
    # MUDA AQUI: 'Usuario' e 'valor_doado' pelos nomes corretos do teu projeto
    lista_de_doadores = Usuario.objects.order_by('nome')
    
    # Se quiseres apenas o "Top 10", por exemplo, podias fazer:
    # lista_de_doadores = Usuario.objects.order_by('-valor_doado')[:10]
    
    # 3. PREPARAR O "CONTEXTO"
    # O contexto é um dicionário que "passa" as nossas variáveis 
    # do Python (a 'lista_de_doadores') para o HTML.
    contexto = {
        'doadores': lista_de_doadores, # 'doadores' será o nome da variável no HTML
    }
    
    # 4. RENDERIZAR O TEMPLATE
    # O Django vai pegar no ficheiro 'doadores.html'
    # e vai "injetar" os dados do 'contexto' nele.
    return render(request, 'doadores.html', contexto)
