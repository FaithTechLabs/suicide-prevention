from . import views
from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
        url(r'^$', views.Index.as_view(), name="index"),
        url(r'^why/', views.Why.as_view(), name="why"),
        url(r'^chat/', views.Chat.as_view(), name="chat"),
        url(r'^why_we_are_here/', views.WhyHere.as_view(), name="why_we_are_here"),
        url(r'^resources/', views.Resource.as_view(), name="resource"),
        url(r'province/(?P<province>[-\w]+)/', views.Province.as_view(), name="resource"),
]
