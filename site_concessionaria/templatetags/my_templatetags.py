from django import template

register = template.Library()

@register.filter
def format_money(value):
    if value >= 1000000:
        return f"{value/1000000:.1f}M"
    elif value >= 1000:
        return f"{value/1000:.1f}k"
    else:
        return str(value)
