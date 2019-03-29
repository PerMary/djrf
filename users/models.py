from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		verbose_name='Пользователь')
	middle_name = models.CharField(
		max_length=200,
		null=False,
		blank=True,
		default='',
		verbose_name='Отчество: ')
