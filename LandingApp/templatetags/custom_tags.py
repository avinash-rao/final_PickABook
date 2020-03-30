from django import template

register = template.Library()

@register.filter
def update_variable(value, newvalue):
    value = newvalue
    return value
