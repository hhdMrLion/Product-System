# Generated by Django 2.2.16 on 2020-12-08 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_auto_20201208_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlist',
            name='created_time',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.SmallIntegerField(choices=[(5, '订单完成'), (1, '备料中'), (2, '待生产'), (3, '生产中'), (4, '待发货')], default=2, verbose_name='订单状态'),
        ),
    ]
