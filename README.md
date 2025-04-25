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
   python manage.py loaddata menu/fixtures/menu.json
   ```
2. **Запустите сервер**:
   ```bash
   python manage.py runserver
   ```
3. **Проверьте админку**:
   - Откройте [http://localhost:8000/admin](http://localhost:8000/admin) и убедитесь, что меню отображается.
4. **Проверьте шаблон**:
   - Откройте [http://localhost:8000](http://localhost:8000)

## Использование
1. Создайте меню в админке.
2. Добавьте пункты меню.
3. В шаблоне:
   ```html
   {% load menu_tags %}
   {% draw_menu 'your_menu' %}
   ```