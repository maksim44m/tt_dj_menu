from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.core.exceptions import ValidationError
from menu.models import Menu, MenuItem
from menu.templatetags.menu.menu_tags import draw_menu

class MenuModelTest(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(name='main_menu')
        self.item1 = MenuItem.objects.create(menu=self.menu, title='Home', url='https://example.com/')
        self.item2 = MenuItem.objects.create(menu=self.menu, title='About', named_url='about', parent=self.item1)

    def test_get_url(self):
        self.assertEqual(self.item1.get_url(), 'https://example.com/')
        self.assertEqual(self.item2.get_url(), reverse('about'))

    def test_validation(self):
        with self.assertRaises(ValidationError):
            MenuItem.objects.create(menu=self.menu, title='Invalid', url='invalid_url')

class MenuTemplateTagTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.menu = Menu.objects.create(name='main_menu')
        self.item1 = MenuItem.objects.create(menu=self.menu, title='Home', url='https://example.com/')
        self.item2 = MenuItem.objects.create(menu=self.menu, title='About', named_url='about', parent=self.item1)

    def test_draw_menu(self):
        request = self.factory.get('/')
        context = {'request': request}
        result = draw_menu(context, 'main_menu')
        self.assertIn('items', result)
        self.assertEqual(len(result['items']), 1)