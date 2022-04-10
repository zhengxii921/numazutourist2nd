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
    image = CloudinaryFileField()

    class Meta:
        model = Place
        fields = "__all__"


class PlaceImageForm(forms.ModelForm):
    class Meta:
        model = PlaceImages
        fields = ['image',]
    image = CloudinaryFileField()

PlaceFormset = forms.inlineformset_factory(Place, PlaceImages, PlaceImageForm, extra=0)


class LovenumaCreateForm(forms.ModelForm):
    image = CloudinaryFileField()
    class Meta:
        model = Lovenuma
        fields = ('place', 'text', 'eva', 'image',)


class LovenumaImageForm(forms.ModelForm):
    image = CloudinaryFileField()
    class Meta:
        model = LovenumaImages
        fields = ['image',]


class LikeCreateForm(forms.ModelForm):

    class Meta:
        model = Like
        fields = []