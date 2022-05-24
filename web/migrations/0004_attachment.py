# Generated by Django 4.0.3 on 2022-04-16 20:46

from django.db import migrations, models
import django.db.models.deletion
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_recipe_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(null=True, upload_to=web.models.attachment_path, verbose_name='File')),
                ('type', models.CharField(blank=True, choices=[('audio', 'Audio'), ('image', 'Image'), ('text', 'Text'), ('video', 'Video'), ('other', 'Other')], default='image', max_length=5, verbose_name='Attachment type')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.recipe')),
            ],
            options={
                'ordering': ['-last_update', 'type'],
            },
        ),
    ]
