# Generated by Django 3.2 on 2023-02-07 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20230202_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='listened',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
