from django import template

register = template.Library()

@register.filter
def get_item_from_list(lst, index):
    if index < len(lst):
        return lst[index]
    return None
