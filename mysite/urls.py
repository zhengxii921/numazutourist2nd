"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from django.utils.decorators import method_decorator

from allauth.account.views import LoginView
from django.views.generic import TemplateView

from axes.decorators import axes_dispatch
from axes.decorators import axes_form_invalid

from mysite.forms import AxesLoginForm

LoginView.dispatch = method_decorator(axes_dispatch)(LoginView.dispatch)
LoginView.form_invalid = method_decorator(axes_form_invalid)(LoginView.form_invalid)

urlpatterns = [
    path("", include("numazutourist.urls")),
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(form_class=AxesLoginForm), name='account_login'),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from numazutourist import views
handler500 = views.my_customized_server_error
