# Generated by Django 4.2.5 on 2023-09-09 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0005_order_shoppingcart_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='unit_price',
        ),
    ]
