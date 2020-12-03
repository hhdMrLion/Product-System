# Generated by Django 2.2.16 on 2020-12-03 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20201203_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='power',
            field=models.SmallIntegerField(choices=[(2, '生产'), (1, '业务'), (3, '商务'), (4, '经理')], default=1, verbose_name='权限'),
        ),
    ]
