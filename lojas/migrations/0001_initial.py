# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-27 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCarrinho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojas.Carrinho')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quandidade', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('quantidade', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojas.Pedido'),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojas.Produto'),
        ),
        migrations.AddField(
            model_name='itemcarrinho',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lojas.Produto'),
        ),
    ]