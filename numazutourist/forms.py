from django import forms
from .models import *
from cloudinary.forms import CloudinaryFileField

class PlaceCreateForm(forms.ModelForm):
    opentime = forms.TimeField(
        label="開店時刻",
        widget=forms.DateInput(attrs={"type":"time"})
    )
    closetime = forms.TimeField(
        label="閉店時刻",
        widget=forms.DateInput(attrs={"type":"time"})
    )
    image = CloudinaryFileField(required=False)

    class Meta:
        model = Place
        fields = "__all__"


class PlaceImageForm(forms.ModelForm):
    class Meta:
        model = PlaceImages
        fields = ['image',]
    image = CloudinaryFileField(required=False)


class LovenumaCreateForm(forms.ModelForm):
    image = CloudinaryFileField()
    class Meta:
        model = Lovenuma
        fields = ('place', 'text', 'eva', 'image',)


class LovenumaImageForm(forms.ModelForm):
    image = CloudinaryFileField(required=False)
    class Meta:
        model = LovenumaImages
        fields = ['image',]


class LikeCreateForm(forms.ModelForm):

    class Meta:
        model = Like
        fields = []


class UserCreateForm(forms.ModelForm):
    profile_picture = CloudinaryFileField(required=False)
    class Meta:
        model = Lovenuma
        fields = ('profile_picture',)

