from django.forms import ModelForm
from .models import Scholar, Mark


class ScholarForm(ModelForm):
	class Meta:
		model = Scholar
		fields = ['first_name',
				'second_name',
				'third_name',
				'grade',
				'date_of_birth',
				'account']


class MarkForm(ModelForm):
	class Meta:
		model: Mark
		fields = '__all__'

