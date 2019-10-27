from django import template
import requests as reqs

register = template.Library()

@register.filter(name='active')
def active(obj, request):
    try: img = obj.url
    except: return False

    path = request.build_absolute_uri(img)
    response = reqs.get(path).status_code

    return False if response != 200 else True
