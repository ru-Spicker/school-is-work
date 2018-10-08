from django.urls import path, reverse

from . import views


urlpatterns = [
	path('', views.index, name='index'),
	path('<int:scholar_id>/diary', views.diary, name='diary'),
	path('<int:scholar_id>/', views.scholar_info, name='info'),
	path('mark_details/<int:pk>', views.MarkDetails.as_view(), name='mark_details'),
	path('mark_create_form', views.MarkCreate.as_view(), name='mark_create'),
	path('mark_update_form/<int:pk>', views.MarkUpdate.as_view(), name='mark_update'),
	path('mark_delete_form/<int:pk>', views.MarkDelete.as_view(), name='mark_delete'),
	]
