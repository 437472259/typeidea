# Generated by Django 2.2.1 on 2019-07-25 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='status',
            field=models.IntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='status',
            field=models.IntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态'),
        ),
    ]
