from django import template

register = template.Library()

@register.filter
def custom_truncate(text, num_chars):
    if len(text) > num_chars:
        return text[:num_chars] + '...'
    return text