# Generated by Django 2.1.4 on 2018-12-18 23:11

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'banner item', 'verbose_name_plural': 'banner item'},
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_desc',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='content'),
        ),
    ]
