from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=128, verbose_name='Полное имя')
    email = models.EmailField(max_length=256, verbose_name='Почта')
    message = models.TextField(max_length=1024, verbose_name='Сообщение')

    def __str__(self):
        return self.full_name
