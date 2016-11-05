from django.shortcuts import render
from django.contrib.gis.geoip import GeoIP
from django.views.generic import TemplateView


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_loc(request):
    g = GeoIP()
    city = g.city(get_client_ip(request))
    province = None
    if city:
        province = city['region']
    return province

class Location:
    template_name = None


class Index(TemplateView, Location):
    template_name = "index.html"

    def get(self, request):
        province = get_loc(request)
        return render(request, self.template_name, {'loc': province})
