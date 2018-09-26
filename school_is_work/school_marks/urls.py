from django.urls import path

from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('<int:scholar_id>/diary', views.diary, name='diary'),
	path('<int:scholar_id>/', views.scholar_info, name='info'),
	path('<int:scholar_id>/add_mark', views.add_mark, name='add_mark'),
	]
