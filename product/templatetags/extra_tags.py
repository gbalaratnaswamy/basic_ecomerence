from django import template

register = template.Library()


@register.filter(name='getdict')
def getdict(value, arg):
    return value.get(str(arg))

