# Generated by Django 2.2.16 on 2020-12-03 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20201203_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.SmallIntegerField(choices=[(4, '订单完成'), (2, '生产中'), (1, '备料中'), (3, '待发货')], default=1, verbose_name='生产状态'),
        ),
    ]