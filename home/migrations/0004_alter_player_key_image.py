# Generated by Django 4.2.7 on 2023-11-25 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_player_key_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player_key',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/img/', verbose_name='Imagem da mira'),
        ),
    ]
