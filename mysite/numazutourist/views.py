from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import PlaceCreateForm, LovenumaCreateForm
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class IndexView(generic.ListView):
    template_name = "numazutourist/index.html"
    model = Lovenuma.objects.order_by("?")[:18] 

    def get_queryset(self):
        return Lovenuma.objects.order_by("?")[:18] 
    

class PlaceListView(generic.ListView):
    model = Place


class PlaceCreateView(generic.CreateView):
    model = Place
    form_class = PlaceCreateForm
    success_url = reverse_lazy("numazutourist:places")


class PlaceDetailView(generic.DetailView):
    model = Place


class PlaceUpdateView(generic.UpdateView):
    model = Place
    form_class = PlaceCreateForm
    success_url = reverse_lazy("numazutourist:places")


class LovenumaListView(generic.ListView):
    model = Lovenuma


class LovenumaCreateView(generic.CreateView):
    model = Lovenuma
    form_class = LovenumaCreateForm
    success_url = reverse_lazy("numazutourist:lovenumazu")


class LovenumaDetailView(generic.DetailView):
    model = Lovenuma


class LovenumaUpdateView(generic.UpdateView):
    model = Lovenuma
    form_class = LovenumaCreateForm
    success_url = reverse_lazy("numazutourist:lovenumazu")


class LovenumaDeleteView(generic.DeleteView):
    model = Lovenuma
    success_url = reverse_lazy("numazutourist:lovenumazu")

