# Generated by Django 5.0.2 on 2024-05-13 10:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula1site', '0004_news_dislikes_news_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=10)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formula1site.news')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formula1site.user')),
            ],
        ),
    ]
