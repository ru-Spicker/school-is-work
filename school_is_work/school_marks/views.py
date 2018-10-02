from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpRequest, HttpResponse
from .models import Scholar, Mark
from django.forms.models import model_to_dict


def index(request):
	scholar_list = get_list_or_404(Scholar.objects.all())
	context = {'scholar_list': scholar_list}
	return render(request, 'school_marks/index.html', context)


def scholar_info(request, scholar_id):
	scholar = get_object_or_404(Scholar, pk=scholar_id)
	marks_set = scholar.mark_set.order_by('-date_of_mark', 'discipline')
	marks = [model_to_dict(mark) for mark in marks_set]
	context = {'scholar': model_to_dict(scholar), 'marks': marks}
	print(context)
	return render(request, 'school_marks/scholar_info.html', context)


def make_marks_table(scholar_id, start_date, end_date):
	pass



def add_mark(request, scholar_id):
	return HttpResponse('Добавление оценки')


def diary(request, scholar_id):
	return HttpResponse('Дневник')
