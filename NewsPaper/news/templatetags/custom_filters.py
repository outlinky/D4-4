from django import template
 
register = template.Library()


@register.filter(name='Censor')
def Censor(value):
    s = str(value.lower())
    l = s.split("редиска")
    s1 = '***'.join(l)
    return s1