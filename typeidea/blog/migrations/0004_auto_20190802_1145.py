# Generated by Django 2.2.3 on 2019-08-02 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190725_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pv',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='post',
            name='uv',
            field=models.PositiveIntegerField(default=1),
        ),
    ]