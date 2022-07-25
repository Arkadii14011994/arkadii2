from statistics import mode
from django.db import models


class ContactUS(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название')
    email= models.EmailField(max_length=255, verbose_name='Почта')
    phone = models.CharField(max_length=255,verbose_name='Номер телефона')
    message = models.TextField(max_length=255,verbose_name='Коментарий')

    def __str__(self) -> str:
        return self.name
