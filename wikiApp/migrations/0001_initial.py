# Generated by Django 5.1 on 2024-08-20 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='temaWiki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTema', models.CharField(blank=True, max_length=128, null=True)),
                ('descripcionTema', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='articuloWiki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tituloArticulo', models.CharField(blank=True, max_length=128, null=True)),
                ('Articulo', models.CharField(blank=True, max_length=1024, null=True)),
                ('temaRelacionado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wikiApp.temawiki')),
            ],
        ),
    ]
