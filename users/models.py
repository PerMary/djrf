from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.contrib.auth.hashers import make_password


class User(AbstractUser):
	username = models.CharField(
		verbose_name='имя пользователя',
		max_length=150,
		blank=True,
		unique=True,
	)
	email = models.EmailField(
		'email',
		unique= True,
	)
	first_name = models.CharField(
		verbose_name='имя',
		max_length=255,
		blank=True,
	)
	last_name =  models.CharField(
		verbose_name='фамилия',
		max_length=255,
		blank=True,
	)

	middle_name = models.CharField(
		verbose_name='отчество',
		max_length=255,
		blank=True,
	)

	objects = UserManager()

	class Meta:
		ordering = ['id']


	def full_name(self):
		if self.middle_name:
			return self.last_name + ' ' + self.first_name + ' ' + self.middle_name
		else:
			return self.first_name + '' + self.last_name


	def short_name(self):
		if self.middle_name:
			return self.first_name[0] + '.' + self.middle_name[0] + '.' + ' ' + self.last_name
		else:
			return self.first_name[0] + '.' + ' ' + self.last_name
    #
	# def set_password(self, raw_password):
	# 	self.password = make_password(raw_password)



