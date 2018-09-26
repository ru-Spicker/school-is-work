from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Scholar


def index(request):
	scholar_list = Scholar.objects.all()
	response = '<br>'.join([scholar.first_name for scholar in scholar_list])
	return HttpResponse('Список учащихся:<br>' + response)


def scholar_info(request, scholar_id):
	scholar = Scholar.objects.get(pk=scholar_id)
	response = f'Информация об учащемся: {scholar.first_name}'
	return HttpResponse(response)


def add_mark(request, scholar_id):
	return HttpResponse('Добавление оценки')


def diary(request, scholar_id):
	return HttpResponse('Дневник')
