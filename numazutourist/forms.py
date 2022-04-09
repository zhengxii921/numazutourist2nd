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
    image = CloudinaryFileField(
            options={'folder': 'media/Model_image', 'tags': 'Model_name'})
            
    class Meta:
        model = Place
        fields = "__all__"


class PlaceImageForm(forms.ModelForm):
    class Meta:
        model = PlaceImages
        fields = ['image',]


PlaceFormset = forms.inlineformset_factory(Place, PlaceImages, PlaceImageForm, extra=0)


class LovenumaCreateForm(forms.ModelForm):
    

    class Meta:
        model = Lovenuma
        fields = ('place', 'text', 'eva', 'image',)


class LovenumaImageForm(forms.ModelForm):
    class Meta:
        model = LovenumaImages
        fields = ['image',]
