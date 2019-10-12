# Generated by Django 2.2.5 on 2019-10-02 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_acceuil_acceuiluser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acceuil',
            old_name='artist',
            new_name='artist1',
        ),
        migrations.RenameField(
            model_name='acceuiluser',
            old_name='artist',
            new_name='artist1',
        ),
        migrations.AddField(
            model_name='acceuil',
            name='artist2',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='acceuiluser',
            name='artist2',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
