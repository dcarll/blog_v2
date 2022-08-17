from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'publicado', 'status')
    list_filter = ('status', 'criado', 'publicado', 'autor')
    
    #inclui uma navegação de pesquisa detalhada pela data
    date_hierarchy = 'publicado'
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug':('titulo',)}

    #permite uma bosca definida pelo campo "autor" pega o ID
    raw_id_fields = ('autor',)

