# Generated by Django 2.1.5 on 2019-02-10 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0005_auto_20190210_0409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curtida',
            name='curtidas',
        ),
    ]
