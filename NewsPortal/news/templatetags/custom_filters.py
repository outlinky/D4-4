from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    STRONG_WORDS = ["php", "редиска"]
    if not isinstance(value, str):
        raise ValueError('Нельзя цензурировать не строку')

    for word in STRONG_WORDS:
        value = value.replace(word[1:], '*' * (len(word) - 1))

    return value
