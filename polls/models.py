from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    # id_usuario = models.IntegerField(primary_key=True, verbose_name='id_usuario')
    nome = models.TextField(max_length=255)
    idade = models.IntegerField(default=0)
    email = models.EmailField()
    mensagem = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Doacao(models.Model):
    id = models.IntegerField(
        primary_key=True, 
        verbose_name="id"
    )

    usuario = models.ForeignKey(
        Usuario,                  # Liga-se ao modelo 'Usuario'
        on_delete=models.CASCADE, # Se o Usuário for apagado, apaga as suas doações
        related_name='doacoes'    # Permite-nos fazer Usuario.doacoes.all()
    )

    valor_doacao = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Valor da Doação"
    )
    
    data_doacao = models.DateField(
        auto_now_add=True, # Preenche automaticamente com a data de hoje
        verbose_name="Data da Doação"
    )

    def __str__(self):
        # Ex: "Ana Silva - R$ 50.00"
        return f"{self.usuario.id} - R$ {self.valor_doacao}"






