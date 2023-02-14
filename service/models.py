from django.db import models
from django.utils.translation import ugettext_lazy as _
from core.models import BaseHistorical


class Contact(BaseHistorical):
    full_name = models.CharField(
        max_length=128,
        verbose_name=_('Полное имя'))
    email = models.EmailField(
        max_length=256,
        verbose_name=_('Почта'))
    message = models.TextField(
        max_length=1024,
        verbose_name=_('Сообщение'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'
