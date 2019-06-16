from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core import validators
from django.db.models import Sum
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

User = get_user_model()



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
        'users.User',
        related_name='demands',
        on_delete=models.CASCADE
    )
    changed = models.BooleanField(
        default=False,
    )


    def __str__(self):
        return self.description


    class Meta:
        ordering = ['id']

    # Подсчет количества позиций
    def position_count(self):
        return Position.objects.filter(demand=self.id).count()

    # Подсчет количесвтва товаров
    def product_count(self):
        prod_count = Position.objects.filter(demand=self.id).aggregate(Sum("quantity"))['quantity__sum']
        if prod_count == None:
            prod_count=0
        return prod_count

    # Подчет общей стоимости всех позиций в зявке
    def price_all(self):
        price_all=0
        positions = Position.objects.filter(demand=self.id)
        for position in positions:
            price_all += position.quantity * position.price_one
        return price_all

    # @classmethod
    # def post_save(cls, sender, created, instance, *args, **kwargs):
    #
    #     Demand.changed =


# post_save.connect(Demand.post_save, sender=Demand)
# @receiver(pre_save, sender=Demand)
# def set_changed(sender, instance, **kwargs):
#     instance.changed = True

# Позиции
class Position(models.Model):
    id = models.AutoField(primary_key=True)

    demand = models.ForeignKey(
        Demand,
        on_delete=models.CASCADE,
        verbose_name='Номер заявки: ',
        related_name='positions',
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
        validators=[validators.MinValueValidator(0)],
    )

    # Подсчет общей стоимости позиции
    def full_price_position(self):
        return (self.quantity * self.price_one)

    def __str__(self):
        return "Позиция " + str(self.id) + ", " + self.name_product

    class Meta:
        ordering = ['id']


@receiver(pre_save, sender=Position)
def position_changed(sender, instance, **kwargs):
    instance.demand.changed = True
    instance.demand.save()


@receiver(pre_delete, sender=Position)
def position_deleted(sender, instance, **kwargs):
    instance.demand.changed = True
    instance.demand.save()

