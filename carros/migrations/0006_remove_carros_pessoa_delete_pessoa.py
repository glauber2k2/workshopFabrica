# Generated by Django 4.1.7 on 2023-04-01 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0005_alter_carros_pessoa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carros',
            name='pessoa',
        ),
        migrations.DeleteModel(
            name='Pessoa',
        ),
    ]
