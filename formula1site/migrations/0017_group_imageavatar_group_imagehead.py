# Generated by Django 5.0.2 on 2024-05-18 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula1site', '0016_alter_meme_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='imageAvatar',
            field=models.ImageField(default=1, upload_to='', verbose_name='Изображение группы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='imageHead',
            field=models.ImageField(default=1, upload_to='', verbose_name='Шапка'),
            preserve_default=False,
        ),
    ]
