from django.db.models import TextChoices
from django.utils.translation import gettext as _


class StatusChoices(TextChoices):
    TO_MODERATE = 'to_moderate', _('На модерацию')
    PUBLISHED = 'published', _('Опубликовано')
    REJECTED = 'rejected', _('Отклонено')


class CategoryChoices(TextChoices):
    AUTO = 'auto', _('Автомобили')
    SERVICE = 'service', _('Услуги')
    SPORT = 'sport', _('Спорт')
    EDUCATION = 'education', _('Образование')
