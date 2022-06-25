from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from webapp.choice import StatusChoices

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name=_('Категория'))

    def __str__(self):
        return {self.title}

    class Meta:
        db_table = 'category'
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')


class Advertisement(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name=_('Заголовок'))
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name=_('Описание'))
    category = models.ForeignKey('webapp.Category', on_delete=models.CASCADE, related_name='advertisement_category',
                                 verbose_name=_('Категория'))
    status = models.CharField(max_length=30, null=False, blank=False, choices=StatusChoices.choices,
                              default='to_moderate', verbose_name=_('Cтатус'))
    picture = models.ImageField(upload_to='pictures/', verbose_name=_('Фото'))
    price = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('Цена'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Автор'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата обновления'))
    published_at = models.DateTimeField(null=True, verbose_name=_('Дата публикации'))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f' {self.author}  {self.title}'

    class Meta:
        db_table = 'advertisement'
        verbose_name = _('Объявление')
        verbose_name_plural = _('Объявления')
