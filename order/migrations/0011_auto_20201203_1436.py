# Generated by Django 2.2.16 on 2020-12-03 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20201203_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.SmallIntegerField(choices=[(2, '待生产'), (4, '待发货'), (1, '备料中'), (3, '生产中')], default=2, verbose_name='订单状态'),
        ),
        migrations.AlterModelTable(
            name='order',
            table='orders',
        ),
    ]
