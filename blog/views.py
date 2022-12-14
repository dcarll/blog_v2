from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Post
from django.contrib.messages.views import SuccessMessageMixin
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.


class BlogListView(ListView):
	'''listar todos as postagens'''
	model = Post
	paginate_by = 8
	template_name = 'blog/home.html'

	


class BLogDetailView(DetailView):
	'''Mostra os detalhes de um post'''
	model = Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'postagem'


class BLogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
	'''Cria um novo post'''
	model = Post
	form_class = PostForm
	template_name = 'blog/post_new.html'
	#fields = ('titulo'	, 'autor', 'conteudo')
	# fields = '__all__' 
	success_message = "%(field)s was created successfully"

	#vericar se o formulario é valido pegar o usuario que esta logado no sistema
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.autor = self.request.user
		obj.save()
		return super().form_valid(form)

	def get_success_message(self, cleaned_data): 
		'''Mensagem de suceeso'''       
		return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )


class BlogUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView ):
	'''Atualiza um post'''
	model = Post
	form_class = PostForm
	template_name = 'blog/post_edit.html'
	#fields = ('titulo', 'conteudo')
	success_message = "%(field)s - foram alterados com sucesso"

	#vericar se o formulario é valido pegar o usuario que esta logado no sistema
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.autor = self.request.user
		obj.save()
		return super().form_valid(form)

	def get_success_message(self, cleaned_data): 
		'''Mensagem de sucesso'''       
		return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )


class BlogDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
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
class Busca(ListView):
    template_name = 'blog/busca.html'	
    model = Post
    context_object_name = 'post'    
	
    def get_queryset(self):    
        qs = super().get_queryset()
        busca = self.request.GET.get('busca')

        if not busca:
            return qs

        qs = qs.filter(
            Q(titulo__icontains=busca) |
            Q(autor__first_name__iexact=busca) |
            Q(conteudo__icontains=busca)

        )

        return qs
