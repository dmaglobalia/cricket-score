# Generated by Django 3.2.8 on 2021-10-12 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0004_auto_20211012_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
