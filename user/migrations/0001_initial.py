# Generated by Django 2.2.16 on 2020-10-28 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
                'ordering': ['-created_time'],
            },
        ),
    ]
