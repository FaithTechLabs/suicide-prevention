from django.contrib.gis.geoip import GeoIP

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_REAL_IP')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    if not ip:
        ip = request.META.get("HTTP_CF_CONNECTING_IP", "")
    return ip

def get_loc(request):
    g = GeoIP()
    city = g.city(get_client_ip(request))
    province = None
    if city:
        province = city['region']
    return province

