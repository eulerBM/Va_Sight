# Generated by Django 4.2.7 on 2023-11-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_player_key_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='player_key',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Imagem da mira'),
        ),
    ]
