from django.db import models


class Scholar(models.Model):
	first_name = models.CharField(max_length=50)
	second_name = models.CharField(max_length=50)
	third_name = models.CharField(max_length=50)
	school_number = models.IntegerField()
	class_number = models.CharField(max_length=5)
	date_of_birth = models.DateField('День рождения')

	def __str__(self):
		return f'{self.second_name} {self.first_name} {self.third_name}'


class Discipline(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name


class Mark(models.Model):
	scholar = models.ForeignKey(Scholar, on_delete=models.CASCADE)
	discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
	date_of_mark = models.DateField()
	volume = models.IntegerField()

	def __str__(self):
		return f'{self.date_of_mark} - {self.scholar.__str__()} - {self.discipline.__str__()} - {self.volume}'

