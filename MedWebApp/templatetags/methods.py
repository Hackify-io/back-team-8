from django import template
from django.templatetags.static import static
from collections import defaultdict

## Metodos capaces de ser usados dentro de HTML = {{ value|split:"," }}
register = template.Library()



def get_url(img_name):
    url = static("imgs/" + img_name)
    return url

register.filter('get_url', get_url, is_safe=False)
