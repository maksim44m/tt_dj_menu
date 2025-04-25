from typing import Any, Dict, List
from django import template
from django.urls import reverse

from menu.models import MenuItem


register = template.Library()


@register.inclusion_tag('menu/menu_item.html', takes_context=True)
def draw_menu(context, menu_name) -> Dict[str, List[Dict[str, Any]]]:
    path = context['request'].path

    items = MenuItem.objects.select_related('parent', 'menu') \
        .filter(menu__name=menu_name) \
        .order_by('order')

    if not items.exists():
        return {'items': []}

    current_item = next(
        (item for item in items if item.get_url() == path),
        None
    )

    active_ids = set()
    if current_item:
        item = current_item
        while item:
            active_ids.add(item.id)
            item = item.parent

    def sort_child(item: MenuItem):
        for child in items:
            if child.parent == item:
                yield child.id in active_ids

    def build_tree(parent: MenuItem = None):
        return [
            {
                'item': item,
                'children': build_tree(item),
                'active': item.id in active_ids,
                'expanded': item.id in active_ids or any(sort_child(item))
            } for item in items if item.parent == parent
        ]
    return {'items': build_tree()}
