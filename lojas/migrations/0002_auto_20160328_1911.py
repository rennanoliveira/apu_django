# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-28 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lojas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='itemcarrinho',
            name='carrinho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_carrinho', to='lojas.Carrinho'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(default='aguardando pagamento', max_length=200),
        ),
    ]
