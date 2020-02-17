from django import template

register = template.Library()

@register.filter(name='is_range')
def is_range(lst):
    return list(range(0, len(lst) - 1))
