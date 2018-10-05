from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpRequest, HttpResponse
from .models import Scholar, Mark, get_current_trimester, get_marks
from django.forms.models import model_to_dict


def index(request):
	scholar_list = get_list_or_404(Scholar.objects.all())
	context = {'scholar_list': scholar_list}
	return render(request, 'school_marks/index.html', context)


def scholar_info(request, scholar_id):
	qs = Scholar.objects.filter(pk=scholar_id).values('first_name', 'second_name', 'grade__name', 'grade__school__name')
	scholar = get_object_or_404(qs)
	trimester = get_current_trimester()
	if trimester:
		marks, earnings = get_marks(scholar_id, trimester.start_date, trimester.end_date)
	print(scholar)
	context = {'scholar': scholar, 'marks': marks, 'earnings': earnings}
	return render(request, 'school_marks/scholar_info.html', context)


def make_marks_table(scholar_id, start_date, end_date):
	pass


def add_mark(request, scholar_id):
	return HttpResponse('Добавление оценки')


def diary(request, scholar_id):
	return HttpResponse('Дневник')
