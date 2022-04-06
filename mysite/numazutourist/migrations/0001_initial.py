# Generated by Django 3.1 on 2022-04-06 09:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weekday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=3, verbose_name='曜日名')),
                ('number', models.IntegerField(unique=True, verbose_name='曜日コード')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('adress', models.CharField(blank=True, max_length=100, null=True, verbose_name='住所')),
                ('explain', models.CharField(blank=True, max_length=140, null=True, verbose_name='施設詳細')),
                ('sort', models.IntegerField(choices=[(1, '飲食店'), (2, 'カフェ/喫茶店'), (3, '軽食'), (4, '自然'), (5, '施設'), (6, 'その他')], verbose_name='種類')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='電話番号')),
                ('opentime', models.TimeField(blank=True, null=True, verbose_name='OPEN')),
                ('closetime', models.TimeField(blank=True, null=True, verbose_name='CLOSE')),
                ('website', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to='numazutourist/', verbose_name='画像')),
                ('holidays', models.ManyToManyField(blank=True, to='numazutourist.Weekday', verbose_name='定休日')),
            ],
        ),
        migrations.CreateModel(
            name='Lovenuma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='名前')),
                ('text', models.TextField(verbose_name='内容')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
                ('eva', models.BooleanField(verbose_name='超良かった')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='numazutourist.place')),
            ],
        ),
    ]
