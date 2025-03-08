# Generated by Django 5.1.6 on 2025-03-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='post_images/image_default.jpg', upload_to='post_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
