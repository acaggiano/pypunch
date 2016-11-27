from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
	url(r'^projects/(?P<project_id>[\d]+)/$', views.projects, name='projects'),
	url(r'^create_project/$', views.new_project, name='new_project'),
]