# Generated by Django 4.1 on 2022-08-21 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chave', models.SlugField(max_length=100, unique=True, verbose_name='Identificação rede')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('url', models.URLField()),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('alterado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
                'ordering': ['chave'],
            },
        ),
    ]
