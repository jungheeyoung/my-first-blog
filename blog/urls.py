from django.conf.urls import url

urlpatterns = [
	url(r'^$','blog.views.post_list'),
	url(r'^(?P<pk>\d+)/$','blog.views.post_detail'),
	url(r'^new/$','blog.views.post_new'),
	url(r'^(?P<pk>\d+)/edit/$','blog.views.post_edit'),

]