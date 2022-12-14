# Generated by Django 4.0.4 on 2022-07-05 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_contacto_task_contacto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='pub_date',
            new_name='release_date',
        ),
        migrations.AlterField(
            model_name='user',
            name='release_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
