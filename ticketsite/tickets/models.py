from django.db import models
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name='Отдел')


class Cabinet(models.Model):
    cabinet = models.CharField(max_length=255, verbose_name='Кабинет')
    dep = models.ForeignKey('Department', on_delete=models.PROTECT, verbose_name='Отдел')


class Ticket_type(models.Model):
    ttype = models.CharField(max_length=255, verbose_name='Тип заявки')


class Ticket_status(models.Model):
    tstatus = models.CharField(max_length=255, verbose_name='Статус')

# class Tickets(models.Model):
#    name = models.CharField(max_length=255, verbose_name='Пользователь')
#    department = models.CharField(max_length=255, verbose_name='Отдел')
#    cabinet = models.CharField(max_length=255, verbose_name='Кабинет')
#    ttype = models.CharField(max_length=255, verbose_name='Тип заявки')
#    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
#    content = models.TextField(blank=True, verbose_name='Текст заявки')
#    tstatus = models.CharField(max_length=255, verbose_name='Статус')
