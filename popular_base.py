#%%
import os
import django
import pandas as pd

#%%
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'siteong.settings')
django.setup()
from polls.models import Usuario, Doacao

#%%
def processar_usuarios(df_usuarios):
    """
    Lê o DataFrame de usuários e cria-os no banco.
    Usa 'get_or_create' para não criar duplicados.
    """
    print(f"\n--- Processando {len(df_usuarios)} usuários ---")
    for indice, linha in df_usuarios.iterrows():
        
        # Pega o nome da coluna 'Nome' do Excel
        id_excel = linha['id_usuario']
        nome_excel = linha['nome']
        idade_excel = linha['idade']
        email_excel = linha['email']
        data_excel = linha['data_cadastro']
        msg_excel = linha['mensagem']
        
        # Procura por um usuário com este nome.
        # Se não encontrar, cria um novo.
        obj, criado = Usuario.objects.get_or_create(
            id_usuario=id_excel
        )
        
        if criado:
            print(f"[CRIADO] Usuário: {obj.id_usuario}")
        else:
            print(f"[JÁ EXISTIA] Usuário: {obj.id_usuario}")

def processar_doacoes(df_doacoes):
    """
    Lê o DataFrame de doações e cria-as no banco,
    ligando-as ao usuário correto.
    """
    print(f"\n--- Processando {len(df_doacoes)} doações ---")
    for indice, linha in df_doacoes.iterrows():
        
        # Pega os valores das colunas do Excel
        id_excel = linha['id']
        valor_excel = linha['valor_doacao']
        data_excel = linha['data_doacao']
        usuario_excel = linha['usuario_id']
        
        try:
            # 1. Encontra o objeto 'Usuario' correspondente
            usuario_obj = Usuario.objects.get(usuario_id=usuario_excel)
            
            # 2. Cria o objeto 'Doacao'
            #    A 'data_doacao' será preenchida automaticamente
            #    pelo 'auto_now_add=True' que definimos no model.
            nova_doacao = Doacao.objects.create(
                usuario=usuario_obj,      # O objeto Usuário
                valor_doacao=valor_excel  # O valor
            )
            print(f"[CRIADA] Doação de R$ {nova_doacao.valor_doacao} para {nova_doacao.usuario.nome}")
        
        except Usuario.DoesNotExist:
            # ERRO: O nome no Excel 'Doacoes' não foi encontrado
            # na tabela 'Usuarios'.
            print(f"[ERRO] Usuário '{nome_usuario_excel}' não encontrado! Pulando esta doação.")
        except Exception as e:
            # Outro erro qualquer
            print(f"[ERRO INESPERADO] {e}")