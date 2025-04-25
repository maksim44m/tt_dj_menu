from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Menu, MenuItem


def get_menu_structure_html(items, parent=None, level=0):
    html = ''
    for item in items.filter(parent=parent):
        url = reverse('admin:menu_menuitem_change', args=[item.id])
        html += f'<li style="margin-left: {level * 20}px"><a href="{url}">{item.title}</a></li>'
        html += get_menu_structure_html(items, parent=item, level=level + 1)
    return html

class EditMenuItemInline(admin.StackedInline):  # Меняем на TabularInline для компактности
    model = MenuItem
    extra = 1
    fields = ('title', 'url', 'named_url', 'parent', 'order')
    show_change_link = True
    verbose_name = "Редактировать пункт"
    verbose_name_plural = "Редактировать текущие пункты"

class MenuAdmin(admin.ModelAdmin):
    inlines = [EditMenuItemInline]
    list_display = ('name', )  # , 'display_structure'
    readonly_fields = ('display_menu_structure', )

    def display_structure(self, obj):
        return '<br>'.join([item.title for item in reversed(obj.items.all())])
    
    
    # display_structure.short_description = 'Текущая структура'
    # display_structure.allow_tags = True

    def display_menu_structure(self, obj):
        items = obj.items.all()
        if not items:
            return 'Нет пунктов меню'
        html = '<ul>'
        html += get_menu_structure_html(items)
        html += '</ul>'
        return format_html(html)
    display_menu_structure.short_description = 'Структура меню'


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem)
