# Generated by Django 2.2.5 on 2019-10-04 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_acceuiluser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='playlist',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='songp',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
