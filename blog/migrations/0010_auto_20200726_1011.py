# Generated by Django 2.0 on 2020-07-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_article_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='titre',
            field=models.CharField(max_length=15),
        ),
    ]
