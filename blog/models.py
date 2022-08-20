from distutils.command.upload import upload
from tabnanny import verbose
from unicodedata import name
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe #para interpreta o html e exibir e imgagem

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                            .filter(status='publicado')

class Category(models.Model):
    nome = models.CharField(max_length=100)
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-criado']

    

    def __str__(self):
        return self.nome

class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )

    titulo = models.CharField(verbose_name='Título', max_length=250)
    slug = models.SlugField(max_length=250)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Category, related_name='get_posts')
    imagem = models.ImageField(upload_to='blog', blank=True, null=True)
    conteudo = RichTextField(verbose_name='Conteúdo')
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                            choices=STATUS,
                            default='rascunho')
    
    
    #como o published foi setado, tem que setar novamente o objects pra ele voltar a funcionar
    objects = models.Manager()

    published = PublishedManager()

    @property
    def view_image(self):
        return mark_safe('<img src="%s" width="400px" />'%self.imagem.url)
        view_image.short_description = "Imagem cadastrada"
        view_image.allow_tags = True

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def get_absolute_url_update(self):
        return reverse('post_edit', args=[self.slug])


    def get_absolute_url_delete(self):
        return reverse('post_delete', args=[self.slug])


    def __str__(self):
        return '{} - {} '.format(self.titulo, self.slug)

    
    class Meta:
        ordering = ('-publicado',)


@receiver(post_save, sender=Post)

def insert_slug(sender, instance, **kwargs):
    '''Preencher atomaticamente o campo de slug'''

    if not instance.slug:
        instance.slug = slugify(instance.titulo)
        return instance.save()
    