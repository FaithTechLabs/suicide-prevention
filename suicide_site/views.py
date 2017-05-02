from django.shortcuts import render
from django.views.generic import TemplateView
from core_site.utils import get_client_ip, get_loc
from .models import Reason

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
        # Gets the province using the IP
        province = get_loc(request)

        # Gets the url the user typed after /province/
        page_loc = kwargs.get('province', '').capitalize().replace("_", " ")

        words = page_loc.split(" ")
        caps = []
        # Fix the names of the provinces
        for word in words:
            if word != "and" and word != "Pei":
                caps.append(word.capitalize())
            elif word == "Pei":
                caps.append("PEI")
            else:
                caps.append(word)
        page_loc = " ".join(caps)

        # Figure out if they typed a proince name or if we need a 404
        if page_loc not in ["Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland", \
                "Nova Scotia", "Ontario", "PEI", "Northwest Territories", "Quebec", "Saskatchewan", "Yukon", "Nunavut"]:
            return render(request, "404.html", {'loc': province, 'page_loc': page_loc})
        return render(request, self.template_name, {'loc': province, 'page_loc': page_loc})


class WhyHere(TemplateView):
    template_name = "why_here.html"

    def get(self, request):
        return render(request, self.template_name)
