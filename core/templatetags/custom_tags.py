from django import template
register = template.Library()

#from ..models import YourModel


@register.filter
def to_float(attendance):
    try:
        float("{}".format(attendance))
    except ValueError:
        return False
    else:
        return True
