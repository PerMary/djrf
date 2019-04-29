from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Заявка
class Demand(models.Model):
    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата создания:',
    )
    id = models.AutoField(primary_key=True)
    description = models.CharField(
        max_length=200,
        verbose_name='Описание заявки:',
        help_text='Закупка оборудования для проекта "Источник И1"',
    )
    user = models.ForeignKey(
        'auth.User',
        related_name='demands',
        on_delete=models.CASCADE
    )
    highlighted = models.TextField()


    def __str__(self):
        return self.description


    # def save(self, *args, **kwargs):
    #     super(Demand,self).save( *args, **kwargs)


    class Meta:
        ordering = ['-created_date']


# Позиции
class Position(models.Model):
    id = models.AutoField(primary_key=True)

    demand = models.ForeignKey(
        Demand,
        on_delete=models.CASCADE,
        verbose_name='Номер заявки: ',
    )
    name_product = models.CharField(
        max_length=50,
        verbose_name='Наименование:',
        help_text='Конденсатор',
    )
    art_product = models.CharField(
        max_length=15,
        verbose_name='Артикул:',
        help_text='AK465JKH7',
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество:',
        help_text='1000',
    )
    price_one = models.FloatField(
        verbose_name='Цена за 1 шт:',
        default=0,
        help_text='0',
    )

    def __str__(self):
        return "Позиция " + str(self.id) + ", " + self.name_product
