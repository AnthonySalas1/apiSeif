# Generated by Django 4.0.5 on 2022-10-28 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_unidad_imagen_alter_unidad_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='passwd',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
