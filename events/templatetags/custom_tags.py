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
