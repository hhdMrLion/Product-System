# Generated by Django 2.2.16 on 2020-12-14 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_auto_20201208_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='owen_num',
        ),
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
    ]
