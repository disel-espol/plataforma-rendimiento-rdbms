from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('results', views.results, name='results'),
	path('progress', views.progress, name='progress'),
	path('ajax/getHwType', views.get_hwType, name='getHwType'),
	path('ajax/getDbSpec', views.get_dbSpec, name='getDbSpec'),
	path('ajax/readFile', views.readFile, name='readFile'),
]