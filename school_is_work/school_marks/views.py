from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpRequest, HttpResponse
from .models import Scholar, Mark, get_current_trimester, get_marks
from .forms import MarkForm
from django.views import generic


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


class MarkDetails(generic.DetailView):
	model = Mark


class MarkCreate(generic.edit.CreateView):
	model = Mark
	template_name_suffix = '_create_form'
	fields = ['scholar', 'discipline', 'date_of_mark', 'mark', 'cost']


def diary(request, scholar_id):
	return HttpResponse('Дневник')
