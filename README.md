# Django Tree Menu

Приложение для создания древовидных меню в Django.

## Миграции
Перед первым запуском примените миграции:
```bash
python manage.py migrate
```

## Проверить работу
1. **Загрузите фикстуры**:
   ```bash
   python manage.py loaddata menu/fixtures/menu_data.json
   ```
2. **Запустите сервер**:
   ```bash
   python manage.py runserver
   ```
3. **Проверьте админку**:
   - Откройте `/admin` и убедитесь, что меню отображается.
4. **Проверьте шаблон**:
   - Добавьте тег `{% draw_menu 'main_menu' %}` в шаблон и откройте страницу.

## Использование
1. Создайте меню в админке.
2. Добавьте пункты меню.
3. В шаблоне:
   ```html
   {% load menu_tags %}
   {% draw_menu 'your_menu' %}
   ```