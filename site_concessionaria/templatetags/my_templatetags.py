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

@register.filter
def mascara_preco_carro(number):
    number_str = f"{number:.2f}"
    integer, decimal = number_str.split(".")
    reversed_integer = integer[::-1]
    formatted_integer = ".".join(reversed_integer[i:i + 3] for i in range(0, len(reversed_integer), 3))[::-1]

    return f"{formatted_integer},00"
