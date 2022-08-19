from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Post
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class BlogListView(ListView):
	'''listar todos as postagens'''
	model = Post
	template_name = 'blog/home.html'


class BLogDetailView(DetailView):
	'''Mostra os detalhes de um post'''
	model = Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'postagem'


class BLogCreateView(SuccessMessageMixin, CreateView):
	'''Cria um novo post'''
	model = Post
	template_name = 'blog/post_new.html'
	fields = ('titulo'	, 'autor', 'conteudo')
	# fields = '__all__'
	success_message = "%(field)s was created successfully"

	def get_success_message(self, cleaned_data): 
		'''Mensagem de suceeso'''       
		return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )


class BlogUpdateView(SuccessMessageMixin, UpdateView ):
	'''Atualiza um post'''
	model = Post
	template_name = 'blog/post_edit.html'
	fields = ('titulo', 'conteudo')
	success_message = "%(field)s - foram alterados com sucesso"

	def get_success_message(self, cleaned_data): 
		'''Mensagem de sucesso'''       
		return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )

class BlogDeleteView(SuccessMessageMixin, DeleteView):
	'''Deleta um post'''
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = reverse_lazy('home')

	success_message = "%(field)s deletado com sucesso"

	def get_success_message(self, cleaned_data): 
		'''Mensagem de sucesso'''       
		return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )
