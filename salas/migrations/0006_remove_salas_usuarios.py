# Generated by Django 4.2.7 on 2023-12-01 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0005_alter_reservas_data_devolucao_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salas',
            name='usuarios',
        ),
    ]
