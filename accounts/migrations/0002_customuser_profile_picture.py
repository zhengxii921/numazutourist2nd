# Generated by Django 3.1 on 2022-04-08 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='numazutourist/orange.jpg', upload_to='numazutourist/icon_images'),
        ),
    ]
