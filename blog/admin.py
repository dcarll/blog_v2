from django.contrib import admin
from .models import Post, Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'publicado', 'status')
    list_filter = ('status', 'criado', 'publicado', 'autor')
    readonly_fields = ('visualizar_image',)    
    #inclui uma navegação de pesquisa detalhada pela data
    date_hierarchy = 'publicado'
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug':('titulo',)}
    #permite uma bosca definida pelo campo "autor" pega o ID
    raw_id_fields = ('autor',)

    def visualizar_image(self, obj):
        return obj.view_image
    visualizar_image.short_description = 'Imagem cadastrada'
    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nome', 'publicado', 'criado')
    list_filter = ('nome', 'publicado', 'criado')    
    #inclui uma navegação de pesquisa detalhada pela data
    date_hierarchy = 'publicado'
    search_fields = ('nome',)