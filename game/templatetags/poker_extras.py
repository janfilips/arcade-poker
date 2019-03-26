import os
import random
import datetime
import json

register = template.Library()


@register.filter(name='dict_get')
def dict_get(h, key):
    try:
        return h[key]
    except:
        return None

@register.filter(name="random_int")
def random_int(a, b=None):
    if b is None:
        a, b = 0, a
    return random.randint(a, b)

