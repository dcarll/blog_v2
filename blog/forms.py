from dataclasses import fields
from tkinter import Widget
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post

class PostForm(forms.ModelForm):
    conteudo = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('titulo', 'conteudo', 'categoria', 'imagem', 'status')
