from django.db import models


class Scholar(models.Model):
	first_name = models.CharField(max_length=50)
	second_name = models.CharField(max_length=50)
	third_name = models.CharField(max_length=50)
	school_number = models.IntegerField()
	class_number = models.CharField(max_length=5)
	date_of_birth = models.DateField('День рождения')


class Discipline(models.Model):
	name = models.CharField(max_length=120)


class Mark(models.Model):
	scholar = models.ForeignKey(Scholar, on_delete=models.CASCADE)
	discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
	date_of_mark = models.DateField()
	volume = models.IntegerField()

	def __str__(self):
		return '{3} - Ученик: {0}\nПредмет: {1} - Оценка: {2}\n'.format(self.scholar.first_name, self.discipline.name, self.volume, self.date_of_mark)

