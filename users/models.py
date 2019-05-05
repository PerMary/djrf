from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		verbose_name='Пользователь')

	lastname = models.CharField(
		max_length=200,
		verbose_name='Фамилия: ',
		help_text='Иванов',
	)
	firstname = models.CharField(
		max_length=150,
		verbose_name='Имя: ',
		help_text='Иван',

	)
	middle_name = models.CharField(
		max_length=200,
		default='',
		verbose_name='Отчество: ',
	    help_text='Иванович',)

