# Generated by Django 3.2.8 on 2021-10-12 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0002_alter_score_wicket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='team_name',
            field=models.CharField(max_length=255),
        ),
    ]
