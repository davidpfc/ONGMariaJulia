from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'idade', 'email', 'mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={'rows': 3}),
        }