# Generated by Django 4.2.5 on 2023-10-28 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cantinho', '0013_alter_pedido_carrinho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='carrinho',
        ),
    ]
