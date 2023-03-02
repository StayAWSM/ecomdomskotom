import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

from core.models import BaseHistorical
from .const import TABLE_NUMBERS, BOOKING_TIME_INTERVALS

from phonenumber_field.modelfields import PhoneNumberField


class Contact(BaseHistorical):
    full_name = models.CharField(
        verbose_name=_('Полное имя'),
        max_length=128
    )
    email = models.EmailField(
        verbose_name=_('Почта'),
        max_length=256
    )
    message = models.TextField(
        verbose_name=_('Сообщение'),
        max_length=1024,
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'


class Booking(BaseHistorical):
    name = models.CharField(
        verbose_name=_('Имя'),
        max_length=128
    )
    phone_number = PhoneNumberField(
        verbose_name=_('Номер телефона'),
        blank=False,
        null=False
    )
    guest_number = models.SmallIntegerField(
        verbose_name=_('Количество гостей'),
        validators=[
            MinValueValidator(1),
            MaxValueValidator(50)
        ],
        blank=False,
        null=False
    )
    comment = models.CharField(
        verbose_name=_('Комментарий'),
        max_length=2048,
        blank=True,
        null=True
    )
    date = models.DateField(
        verbose_name=_('Дата'),
        default=datetime.date.today(),
        blank=False,
        null=False
    )
    time_from = models.TimeField(
        verbose_name=_('Время от'),
        choices=BOOKING_TIME_INTERVALS,
        blank=False,
        null=False,
    )
    time_to = models.TimeField(
        verbose_name=_('Время до'),
        choices=BOOKING_TIME_INTERVALS,
        blank=False,
        null=False
    )
    table_number = models.SmallIntegerField(
        verbose_name=_('Номер стола'),
        choices=TABLE_NUMBERS,
        blank=False,
        null=False
    )

    def __str__(self):
        return f'{self.name}/{self.date}/{self.time_from}/{self.table_number}'

    # def clean(self):
    #     if self.time_from > self.time_to:
    #         raise ValidationError('Некорректное время бронирования:'
    #                               'время С превышает время ПО.')
    #     if self.date < datetime.date.today():
    #         raise ValidationError('Некорректная дата бронирования.')

    def save(self, *args, **kwargs):
        if self.time_from > self.time_to:
            raise ValidationError('Некорректное время бронирования:'
                                  'время С превышает время ПО.')
        if self.date < datetime.date.today():
            raise ValidationError('Некорректная дата бронирования.')
        else:
            super(Booking, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Бронирование')
        verbose_name_plural = _('Бронирование')
