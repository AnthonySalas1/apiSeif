# Generated by Django 4.0.4 on 2022-07-05 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_task_contacto_task_link_alter_task_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Contacto',
            new_name='contacto',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='Descripcion',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='Direccion',
            new_name='direccion',
        ),
    ]
