from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _


class MyUser(AbstractUser):
    phone = PhoneNumberField(region="KG", max_length=13, verbose_name=_('Номер телефона'))

    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.pk})
