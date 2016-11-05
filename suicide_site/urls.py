from . import views
from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
        url(r'^$', views.Index.as_view(), name="index"),
        url(r'^why/', views.Why.as_view(), name="why")
]
