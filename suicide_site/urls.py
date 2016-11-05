from . import views
from django.conf.urls import include, url

urlpatterns = [
        url(r'^$', views.index, name="index")
]
