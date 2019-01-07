from django.contrib.gis.geoip import GeoIP
from .utils import get_client_ip

def geoip(request):
    # Allow passing a test IP
    ip = get_client_ip(request)

    try:
        info = GeoIP().city(ip)
    except Exception as e:
        info = {}

    return { "geo": info }

