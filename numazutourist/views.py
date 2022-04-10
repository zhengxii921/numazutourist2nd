from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import PlaceCreateForm, LovenumaCreateForm, UserCreateForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
import sys
sys.path.append('../')
from accounts.models import CustomUser
from django.shortcuts import redirect, get_object_or_404
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


class PlaceUpdateView(LoginRequiredMixin, generic.UpdateView):
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


class LovenumaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Lovenuma
    form_class = LovenumaCreateForm
    success_url = reverse_lazy("numazutourist:lovenumazu")

    def get_queryset(self):
        base_qs = super(LovenumaUpdateView, self).get_queryset()
        # さらにユーザIDで絞った結果を返す。(存在しないので404が返る)
        # 条件分岐してエラーページを出しても可
        return base_qs.filter(user=self.request.user)


class LovenumaDeleteView(generic.DeleteView):
    model = Lovenuma
    success_url = reverse_lazy("numazutourist:lovenumazu")


class UserDetailView(generic.DetailView):
    model = get_user_model()

class UserUpdateView(generic.UpdateView):
    model = get_user_model()
    form_class = UserCreateForm
    success_url = reverse_lazy("numazutourist:lovenumazu")

    def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)


from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseServerError

@requires_csrf_token
def my_customized_server_error(request, template_name='500.html'):
    import sys
    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)


def like(request, pk):
    lovenuma = get_object_or_404(Lovenuma, pk=pk)
    Like.objects.create(lovenuma=lovenuma, user=request.user)
    return redirect("numazutourist:lovenumazu")