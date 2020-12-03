# Generated by Django 2.2.16 on 2020-12-03 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201118_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='power',
            field=models.SmallIntegerField(choices=[(4, '经理'), (1, '业务'), (2, '生产'), (3, '商务')], default=1, verbose_name='权限'),
        ),
    ]