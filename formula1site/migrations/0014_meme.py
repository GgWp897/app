# Generated by Django 5.0.2 on 2024-05-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula1site', '0013_user_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='текст мемаса')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_memes', to='formula1site.user')),
            ],
        ),
    ]
