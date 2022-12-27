# coding=utf-8

from django.db import models


class Object(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name='Номер Объекта', unique=True)

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'
        ordering = ['number', ]

    def __str__(self):
        return f"Объект номер:  {self.number}"

    def agent_url(self):
        url = f"http://127.0.0.1:8000/admin/db_main/agent/?q={self.number}"
        from django.utils.html import format_html
        return format_html("<a href='%s'>%s</a>" % (url, 'Ответственные'))


    def pasport_url(self):
        url = f"http://127.0.0.1:8000/admin/db_main/objectpasport/?q={self.number}"
        from django.utils.html import format_html
        return format_html("<a href='%s'>%s</a>" % (url, 'Паспорт'))

    agent_url.short_description = 'Ответственные'
    pasport_url.short_description = 'Паспорт'


class ObjectPasport(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, verbose_name='Номер Объекта')
    name = models.CharField(verbose_name='Имя Объекта', max_length=100)
    address = models.CharField(verbose_name='Адрес Объекта', max_length=100, blank=True)
    gsm1 = models.CharField(verbose_name='1й Телефон прибора', max_length=100, blank=True)
    gsm2 = models.CharField(verbose_name='2й Телефон прибора', max_length=100, blank=True)
    guard = models.CharField(verbose_name='Охрана', max_length=100, blank=True)
    type = models.CharField(verbose_name='Тип прибора', max_length=100, blank=True)
    guard_car = models.CharField(verbose_name='Машина охраны', max_length=100, blank=True)
    guard_period = models.CharField(verbose_name='Период охраны', max_length=100, blank=True)
    event1 = models.CharField(verbose_name='Время постановки', max_length=50, blank=True)
    event2 = models.CharField(verbose_name='Время снятия', max_length=50, blank=True)
    priority = models.CharField(verbose_name='Приоритет', max_length=20, blank=True)
    contact = models.CharField(verbose_name='Контакты', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Паспорт объекта'
        verbose_name_plural = 'Паспорта объектов'

    def __str__(self):
        return f"{self.object}  /  {self.name}"


class ObjectState(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, verbose_name='Номер Объекта')
    monitor = models.BooleanField(verbose_name='Мониторинг')
    guard = models.BooleanField(verbose_name='Охрана')
    on_off = models.BooleanField(verbose_name='Включен')
    silent = models.BooleanField(verbose_name='Тишина')
    alarm = models.BooleanField(verbose_name='Тревога')
    battery = models.BooleanField(verbose_name='Батарея')
    power = models.BooleanField(verbose_name='Питание')
    tamper = models.BooleanField(verbose_name='Тампер')

    class Meta:
        verbose_name = 'Состояние объекта'
        verbose_name_plural = 'Состояние объектов'

    def __str__(self):
        return f"{self.object} | {'На охране' if self.guard else 'Снят'}| " \
               f"Мониторинг {'Вкл' if self.monitor else 'Выкл'}"



class Agent(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, verbose_name='Номер Объекта')
    number = models.PositiveSmallIntegerField('Номер')
    name = models.CharField(max_length=100, verbose_name='Имя')
    role = models.CharField(max_length=200, blank=True, verbose_name='Статус')
    address = models.CharField( max_length=200, blank=True, verbose_name='Адрес')
    phone = models.CharField( max_length=100, blank=True, verbose_name='Телефон')
    sms_phone = models.CharField( max_length=15, blank=True, verbose_name='СМС номер')
    info = models.CharField( max_length=200, blank=True, verbose_name='Другое')

    #list_display = ("object", "number")

    def __str__(self):
        return f"{self.object}:  Ответственный {self.number}, {self.name}, {self.role}, {self.phone}"

    class Meta:
        verbose_name = 'Ответственный'
        verbose_name_plural = 'Ответственные'
        ordering = ['object', 'number', ]
        unique_together = ('object', 'number')
        #app_label = 'my_app_name'


class Partition(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, verbose_name='Номер Объекта')
    number = models.PositiveSmallIntegerField('Номер')
    guard = models.BooleanField(verbose_name='Охрана')
    info = models.CharField(max_length=100, verbose_name='Информация')

    def __str__(self):
        return f"{self.object}:  Раздел {self.number}, {self.guard}, {self.info}"

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['object', 'number', ]
        unique_together = ('object', 'number')
        #app_label = 'my_app_name'


class SmsPhone(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, verbose_name='Номер Объекта')
    phone = models.CharField(max_length=20, verbose_name='Номер СМС оповещения')

    def __str__(self):
        return f"{self.object}:  Номер СМС оповещения {self.phone}"

    class Meta:
        verbose_name = 'Номер для СМС'
        verbose_name_plural = 'Номера для СМС'
        unique_together = ('object', 'phone')
        ordering = ['object', 'phone', ]
        #app_label = 'my_app_name'


class Zone(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, verbose_name='Номер Объекта')
    Zone = models.TextField(verbose_name='Зона')

 #   def __str__(self):
 #       return f"{self.object}:  Зона {self.phone}"

    class Meta:
        verbose_name = 'Зона'
        verbose_name_plural = 'Зоны'
#        unique_together = ('object', 'phone')
#        ordering = ['object', 'phone', ]
