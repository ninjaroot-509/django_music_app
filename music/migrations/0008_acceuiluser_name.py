# Generated by Django 2.2.5 on 2019-10-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20191003_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='acceuiluser',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
