# Generated by Django 2.2.16 on 2020-12-03 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20201203_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_list_id', models.CharField(blank=True, max_length=6, null=True, verbose_name='配件单id')),
                ('good', models.CharField(max_length=128, verbose_name='产品名称')),
                ('number', models.IntegerField(verbose_name='数量')),
            ],
            options={
                'verbose_name': '所有订单配件信息',
                'verbose_name_plural': '所有订单配件信息',
                'db_table': 'order_list',
                'ordering': ['order_list_id'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True, verbose_name='订单id'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.SmallIntegerField(choices=[(1, '备料中'), (2, '待生产'), (3, '生产中'), (4, '待发货')], default=2, verbose_name='订单状态'),
        ),
    ]
