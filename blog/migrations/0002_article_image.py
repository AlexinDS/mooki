# Generated by Django 3.0.8 on 2020-07-06 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=1, upload_to='img'),
            preserve_default=False,
        ),
    ]
