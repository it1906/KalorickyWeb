# Generated by Django 4.0.3 on 2022-04-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
