from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.contrib.auth.hashers import make_password

# class Profile(models.Model):
# 	user = models.OneToOneField(
# 		User,
# 		on_delete=models.CASCADE,
# 		verbose_name='Пользователь')
#
# 	lastname = models.CharField(
# 		max_length=200,
# 		verbose_name='Фамилия: ',
# 		help_text='Иванов',
# 	)
# 	firstname = models.CharField(
# 		max_length=150,
# 		verbose_name='Имя: ',
# 		help_text='Иван',
#
# 	)
# 	middle_name = models.CharField(
# 		max_length=200,
# 		default='',
# 		verbose_name='Отчество: ',
# 	    help_text='Иванович',)
#
# 	class Meta:
# 		ordering = ['id']



#Как убрать профиль и вместо него использовать расширенный менеджер пользователя?

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
    #
	# def set_password(self, raw_password):
	# 	self.password = make_password(raw_password)



