# Generated by Django 2.2.16 on 2020-11-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20201106_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='sn',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='订单编号'),
        ),
    ]
