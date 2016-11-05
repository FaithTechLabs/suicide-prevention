from . import views
from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
        url(r'^$', views.Index.as_view(), name="index")
]
