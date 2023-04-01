# Generated by Django 4.1.7 on 2023-04-01 00:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0003_remove_carros_pessoa_delete_pessoa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id_pessoa', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='carros',
            name='pessoa',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='carros.pessoa'),
        ),
    ]
