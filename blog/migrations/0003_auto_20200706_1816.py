# Generated by Django 3.0.8 on 2020-07-06 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image',
            new_name='photo',
        ),
    ]
