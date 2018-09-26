from django.db import models


class Scholar(models.Model):
	first_name = models.CharField('Имя', max_length=50)
	second_name = models.CharField('Фамилия', max_length=50)
	third_name = models.CharField('Отчество', max_length=50)
	school_number = models.IntegerField('Номер школы')
	class_number = models.CharField('Класс', max_length=5)
	date_of_birth = models.DateField('День рождения')
	account = models.IntegerField('Очки', default=0)

	def __str__(self):
		return f'{self.second_name} {self.first_name} {self.third_name}'

	class Meta:
		verbose_name = 'Учащийся'
		verbose_name_plural = 'Учащиеся'


class MarksCost(models.Model):

	'''Define cost each school mark'''

	name = models.CharField('Название', max_length=30)
	start_date = models.DateField('Действует с')
	end_date = models.DateField('Действует до')
	fine_cost = models.IntegerField('Отлично')
	good = models.IntegerField('Хорошо')
	satisfactory = models.IntegerField('Удовлетворительно')
	unsatisfactory = models.IntegerField('Неудовлетворительно')
	unacceptable = models.IntegerField('Неприемлемо')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Система оценок'
		verbose_name_plural = 'Системы оценок'


class Discipline(models.Model):
	name = models.CharField('Предмет', max_length=120)
	cur_cost = models.ForeignKey(MarksCost, on_delete=models.PROTECT, null=True, verbose_name='Система оценок')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Предмет'
		verbose_name_plural = 'Предметы'


class Mark(models.Model):
	scholar = models.ForeignKey(Scholar, on_delete=models.CASCADE, verbose_name='Учащийся')
	discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Предмет')
	date_of_mark = models.DateField('Дата')
	mark = models.IntegerField('Оценка')
	cost = models.IntegerField('Цена')

	def __str__(self):
		return f'{self.date_of_mark} - {self.scholar.__str__()} - {self.discipline.__str__()} - {self.mark}'

	class Meta:
		verbose_name = 'Оценка'
		verbose_name_plural = 'Оценки'
