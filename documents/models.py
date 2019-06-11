from django.db import models
from django.utils import timezone
from django.conf import settings
from users.models import User
from demands.models import Demand

class Document (models.Model):
    date_create = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата создания',
    )
    user_create = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    demand = models.ForeignKey(
        Demand,
        on_delete=models.CASCADE,
        verbose_name = 'Заявка',
    )
    name_doc = models.CharField(
        max_length=50,
        verbose_name='Название документа',
    )
    url = models.CharField(
        max_length=250,
        verbose_name='Ссылка документа'
    )


    def __str__ (self):
        return "PDF документ к заявке №" + str(self.demand.id)

    class Meta:
        ordering = ['-date_create']