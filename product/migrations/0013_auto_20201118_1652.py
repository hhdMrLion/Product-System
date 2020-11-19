# Generated by Django 2.2.16 on 2020-11-18 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20201116_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '备料中'), (2, '生产中'), (4, '订单完成'), (3, '待发货')], default=1, verbose_name='生产状态'),
        ),
    ]