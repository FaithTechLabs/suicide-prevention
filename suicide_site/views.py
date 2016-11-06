from django.shortcuts import render
from django.contrib.gis.geoip import GeoIP
from django.views.generic import TemplateView
from .models import Reason


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_REAL_IP')
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


class Chat(TemplateView, Location):
    template_name = "chat.html"

    def get(self, request):
        province = get_loc(request)
        return render(request, self.template_name, {'loc': province})


class Resource(TemplateView, Location):
    template_name = "resource.html"

    def get(self, request):
        province = get_loc(request)
        return render(request, self.template_name, {'loc': province})


class Province(TemplateView, Location):
    template_name = "province.html"

    def get(self, request, **kwargs):
        province = get_loc(request)
        page_loc = kwargs.get('province', '').capitalize().replace("_", " ")
        words = page_loc.split(" ")
        caps = []
        for word in words:
            if word != "and" and word != "Pei":
                caps.append(word.capitalize())
            elif word == "Pei":
                caps.append("PEI")
            else:
                caps.append(word)
        page_loc = " ".join(caps)

        print(page_loc)
        if page_loc not in ["Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland", \
                "Nova Scotia", "Ontario", "PEI", "Northwest Territories", "Quebec", "Saskatchewan", "Yukon", "Nunavut"]:
            return render(request, "404.html", {'loc': province, 'page_loc': page_loc})
        return render(request, self.template_name, {'loc': province, 'page_loc': page_loc})


class Why(TemplateView, Location):
    template_name = "why.html"

    def get(self, request):
        province = get_loc(request)
        return render(request, self.template_name, {'loc': province})

    def post(self, request):
        province = get_loc(request)
        print(request.POST.get("why", ""))
        #In order to be any good we'll need to move to psql, after we do that when can use __search for this
        query = Reason.objects.filter(keywords__search=str(request.POST.get("why", ""))).first()
        if not query:
            answers = ""
            resources = ""
            return render(request, self.template_name, {'loc': province, 'answers': answers, 'resources': resources })

        answers = query.response
        resources = query.resources.split("\n")
        return render(request, self.template_name, {'loc': province, 'answers': answers, 'resources': resources })

class WhyHere(TemplateView):
    template_name = "why_here.html"

    def get(self, request):
        return render(request, self.template_name)
