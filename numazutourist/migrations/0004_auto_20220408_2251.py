# Generated by Django 3.1 on 2022-04-08 13:51

from django.db import migrations, models
import django.db.models.deletion
import numazutourist.models


class Migration(migrations.Migration):

    dependencies = [
        ('numazutourist', '0003_auto_20220408_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lovenuma',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=numazutourist.models.lovenuma_image_directory_path, verbose_name='画像'),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=numazutourist.models.place_image_directory_path, verbose_name='画像'),
        ),
        migrations.CreateModel(
            name='PlaceImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=numazutourist.models.place_image_directory_path)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_images', to='numazutourist.place')),
            ],
        ),
        migrations.CreateModel(
            name='LovenumaImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=numazutourist.models.lovenuma_image_directory_path)),
                ('lovenuma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lovenuma_images', to='numazutourist.lovenuma')),
            ],
        ),
    ]
