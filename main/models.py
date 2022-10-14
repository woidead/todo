from datetime import datetime
from tabnanny import verbose
from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length = 40, verbose_name = 'Название')
    description = models.TextField(verbose_name = 'Описание')
    sent_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата и время ')

class Delete(models.Model):
    deleted_title = models.CharField(max_length = 40, verbose_name = 'Название')
    deleted_description = models.TextField(verbose_name = 'Описание')
    deleted_sent_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата и время ')

class Favourites(models.Model):
    favourite_title = models.CharField(max_length = 40, verbose_name = 'Название')
    favourite_description = models.TextField(verbose_name = 'Описание')
    favourite_sent_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата и время ')