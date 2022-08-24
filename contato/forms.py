from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'placeholder':'Nome'}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'placeholder':'Digite seu a-mail'}))
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'placeholder':'Assunto'}))