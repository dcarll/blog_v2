# Generated by Django 4.1 on 2022-08-20 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_categoria_alter_post_options_post_imagem_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Category',
        ),
    ]