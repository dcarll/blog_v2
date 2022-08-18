from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Post

# Create your views here.
class BlogListView(ListView):
	model = Post
	template_name = 'blog/home.html'

class BLogDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'
	context_object_name = 'postagem'

class BLogCreateView(CreateView):
	model = Post
	template_name = 'blog/post_new.html'
	fields = ('titulo', 'slug', 'autor')
	# fields = '__all__'

class BlogUpdateView(UpdateView):
	model = Post
	template_name = 'blog/post_edit.html'
	fields = ('titulo', 'conteudo')

class BlogDeleteView(DeleteView):
	model = Post
	template_name = 'blog/post_delete.html'
	success_url = reverse_lazy('home')
