from django import template
import requests

register = template.Library()

@register.filter(name='active')
def active(url, request):
    path = request.build_absolute_uri(url)
    if requests.get(path).status_code != 200:
        return False
    return True
