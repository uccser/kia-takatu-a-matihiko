"""Module for the custom get_item template tag."""

from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """Return the value for a key in the dictionary.

    Args:
        dictionary (dict): Dictionary to use for lookup.
        key (str): String of key for lookup.

    Returns:
        Value for key.
    """
    return dictionary.get(key)
