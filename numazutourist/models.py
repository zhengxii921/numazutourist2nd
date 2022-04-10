from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.contrib.auth import get_user_model
import uuid
from django.core.files.base import ContentFile
from sorl.thumbnail import get_thumbnail, delete
from cloudinary.models import CloudinaryField

# Create your models here.


class Weekday(models.Model):
    name = models.CharField(
        verbose_name="曜日名",
        max_length=3
    )
    number = models.IntegerField(
        verbose_name="曜日コード",
        unique=True
    )
    def __str__(self) -> str:
        return f'{self.name}'

def place_image_directory_path(instance, filename):
    return 'numazutourist/place_images/{}.{}'.format(str(uuid.uuid4()), filename.split('.')[-1])

class Place(models.Model):

    SORT_CHOICES = (
        (1, "飲食店"),
        (2, "カフェ/喫茶店"),
        (3, "軽食"),
        (4, "自然"),
        (5, "施設"),
        (6, "その他"),
    )

    name = models.CharField("名称",max_length=30)
    adress = models.CharField("住所",max_length=100, blank=True, null=True)
    explain = models.CharField("施設詳細", max_length=140, blank=True, null=True)
    sort = models.IntegerField("種類",choices=SORT_CHOICES)
    is_sacred = models.BooleanField(verbose_name="ラブライブ!聖地", default=False)
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    phonenumber = models.CharField(validators=[tel_number_regex], max_length=15, verbose_name='電話番号', unique=True, blank=True, null=True)
    holidays = models.ManyToManyField(Weekday, verbose_name="定休日", blank=True)
    opentime = models.TimeField("OPEN", blank=True, null=True)
    closetime = models.TimeField("CLOSE", blank=True, null=True)
    website = models.URLField("URL", blank=True, null=True)
    image = CloudinaryField(verbose_name="画像", blank=True, null=True, folder=place_image_directory_path)

    def __str__(self):
        return self.name


class PlaceImages(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="place_images")
    image = CloudinaryField("画像", blank=True, null=True, folder=place_image_directory_path)



def lovenuma_image_directory_path(instance, filename):
    return 'numazutourist/place_images/{}.{}'.format(str(uuid.uuid4()), filename.split('.')[-1])

class Lovenuma(models.Model):

    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField("内容")
    date = models.DateTimeField("投稿日時", default=timezone.now)
    eva = models.BooleanField("超良かった")
    image = CloudinaryField("画像", blank=True, null=True, folder=lovenuma_image_directory_path)


    def __str__(self):
        return self.text


class Like(models.Model):
    lovenuma = models.ForeignKey(Lovenuma, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)


class LovenumaImages(models.Model):
    lovenuma = models.ForeignKey(Lovenuma, on_delete=models.CASCADE, related_name="lovenuma_images")
    image = CloudinaryField("画像", blank=True, null=True, folder=lovenuma_image_directory_path)