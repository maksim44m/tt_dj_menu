from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

class Menu(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    url = models.CharField(max_length=256, blank=True)
    named_url = models.CharField(max_length=256, null=True, blank=True)
    parent = models.ForeignKey('self', 
                               on_delete=models.CASCADE, 
                               null=True, 
                               blank=True,
                               related_name='children')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except:
                return self.url or "#"
        return self.url or "#"

    def clean(self) -> None:
        if not self.url and not self.named_url:
            raise ValidationError("Должно быть заполнено хотя бы одно поле: URL или Named URL.")
        
        if self.url:
            validator = URLValidator()
            try:
                validator(self.url)
            except ValidationError:
                raise ValidationError({"url": "Некорректный URL. Пример: https://example.com"})
        
        if self.named_url:
            try:
                reverse(self.named_url)
            except:
                raise ValidationError({"named_url": "Некорректное имя URL. Проверьте, что такой URL существует."})

    def save(self, *args, **kwargs):
        if not self.order:
            last_item = MenuItem.objects.filter(menu=self.menu, parent=self.parent).order_by('-order').first()
            self.order = last_item.order + 1 if last_item else 1
        self.full_clean()
        super().save(*args, **kwargs)

