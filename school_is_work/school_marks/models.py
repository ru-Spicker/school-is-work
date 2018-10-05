from django.db import models
from django.utils import timezone


class School(models.Model):
	name = models.CharField('Название', max_length=120)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Школа'
		verbose_name_plural = 'Школы'


class Grade(models.Model):
	name = models.CharField('Класс', max_length=3, default='')
	school = models.ForeignKey(School, on_delete=models.PROTECT, null=True, verbose_name='Школа')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Класс'
		verbose_name_plural = 'Классы'


class Scholar(models.Model):
	first_name = models.CharField('Имя', max_length=50)
	second_name = models.CharField('Фамилия', max_length=50)
	third_name = models.CharField('Отчество', max_length=50)
	grade = models.ForeignKey(Grade, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Класс')
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


class Trimester(models.Model):
	number = models.IntegerField('Триместр', default=1)
	start_date = models.DateField('Дата начала', default=timezone.now())
	end_date = models.DateField('Дата окончания', default=timezone.now())

	def __str__(self):
		return f'№{self.number}\t{self.start_date} - {self.end_date}'

	class Meta:
		verbose_name = 'Триместр'
		verbose_name_plural = 'Триместры'


def get_current_trimester(date=timezone.now()):
	"""Returns a Trimester object that includes the specified date
	If the specified date is not included in any Trimester, returns the last Trimester
	that began before the specified date."""

	cur_trimester = Trimester.objects.filter(start_date__lte=date, end_date__gte=date)
	if not cur_trimester:
		cur_trimester = Trimester.objects.filter(start_date__lte=date)
	if cur_trimester.exists():
		return cur_trimester[0]
	else:
		return None


def get_marks(scholar, start_date, end_date, discipline=None):
	if discipline:
		marks = Mark.objects.filter(scholar_id=scholar, date_of_mark__gte=start_date, date_of_mark__lte=end_date,
					discipline=discipline).values(
					'discipline', 'date_of_mark', 'mark', 'cost').order_by('-date_of_mark')
	else:
		marks = Mark.objects.filter(scholar_id=scholar,
									date_of_mark__gte=start_date, date_of_mark__lte=end_date).values(
									'discipline__name', 'date_of_mark', 'mark', 'cost').order_by('-date_of_mark')

	earnings = {}
	for mark in marks:
		if mark['discipline__name'] in earnings:
			earnings[mark['discipline__name']] += mark['cost']
		else:
			earnings[mark['discipline__name']] = mark['cost']
	earnings['Итого'] = sum(earnings.values())

	print(earnings)

	table = {m['date_of_mark']: {} for m in marks}
	for m in marks: table[m['date_of_mark']] = {m['discipline__name']: [] for m in marks}
	for m in marks: table[m['date_of_mark']][m['discipline__name']].append(m['mark'])
	for key, item in table.items():
		print(str(key) + '\t' + repr(item))

	return table, earnings

