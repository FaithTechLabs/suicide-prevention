from django.shortcuts import render
from django.contrib.gis.geoip import GeoIP
from django.views.generic import TemplateView
from .models import Reason


def get_client_ip(request):
    ip = request.META.get('HTTP_CF_CONNECTING_IP')
    if ip is None:
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

class Chat(TemplateView, Location):
    template_name = "chat.html"

    def get(self, request):
        province = get_loc(request)
        return render(request, self.template_name, {'loc': province})


class Why(TemplateView, Location):
    template_name = "why.html"

    def get(self, request):
        province = get_loc(request)
        return render(request, self.template_name, {'loc': province})

    def post(self, request):
        province = get_loc(request)
        print(request.POST.get("why", ""))
        query = Reason.objects.filter(keywords__icontains=request.POST.get("why", "")).first()
        if not query:
            answers = ""
            resources = ""
            return render(request, self.template_name, {'loc': province, 'answers': answers, 'resources': resources })

        answers = query.response
        resources = query.resources.split("\n")
        return render(request, self.template_name, {'loc': province, 'answers': answers, 'resources': resources })
