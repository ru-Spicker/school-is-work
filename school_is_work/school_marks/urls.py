from django.urls import path, reverse

from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('<int:scholar_id>/diary', views.diary, name='diary'),
	path('<int:scholar_id>/', views.scholar_info, name='info'),
	path('mark_details/<int:pk>', views.MarkDetails.as_view(), name='mark_details'),
	path('mark_create_form', views.MarkCreate.as_view(), name='mark_create'),
	]
