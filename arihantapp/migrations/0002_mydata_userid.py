# Generated by Django 2.2.11 on 2021-12-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arihantapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mydata',
            name='userid',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
