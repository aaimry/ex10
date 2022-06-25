from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _


class User(AbstractUser):
    phone = PhoneNumberField(region="KG", max_length=13, verbose_name=_('Номер телефона'))
