from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import PlaceCreateForm, LovenumaCreateForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
import sys
sys.path.append('../')
from accounts.models import CustomUser
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
    paginate_by = 30
    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Lovenuma.objects.filter(
                Q(place__name__icontains=q_word) | Q(text__icontains=q_word)
            )
        else:
            object_list = Lovenuma.objects.all()
        return object_list


class LovenumaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Lovenuma
    form_class = LovenumaCreateForm
    success_url = reverse_lazy("numazutourist:lovenumazu")

    def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)

class LovenumaDetailView(generic.DetailView):
    model = Lovenuma


class LovenumaUpdateView(generic.UpdateView):
    model = Lovenuma
    form_class = LovenumaCreateForm
    success_url = reverse_lazy("numazutourist:lovenumazu")


class LovenumaDeleteView(generic.DeleteView):
    model = Lovenuma
    success_url = reverse_lazy("numazutourist:lovenumazu")


class UserDetailView(generic.DetailView):
    model = get_user_model()

    