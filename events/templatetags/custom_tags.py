# events/templatetags/custom_tags.py
from django import template

register = template.Library()

@register.filter
def dict_get(d, key):
    """Get dictionary value by key safely."""
    if isinstance(d, dict):
        try:
            return d.get(int(key)) or d.get(str(key)) or 0
        except Exception:
            return 0
    return 0

@register.filter
def split(value, sep=","):
    return [s for s in value.split(sep) if s]

@register.filter
def ordinal(value):
    try:
        n = int(value)
    except (TypeError, ValueError):
        return value
    if 10 <= n % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"