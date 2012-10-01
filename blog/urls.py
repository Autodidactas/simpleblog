from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from models import *

urlpatterns = patterns('blog.views',
	url(r'^$', 'index', name="lista"),
	url(r'^lista/$', ListView.as_view(model=Posts,
					template_name='blog/blog_list.html',
					paginate_by=3)
					, name="blog_list"),
	url(r'^blog/(?P<slug>[-\w]+)/$', DetailView.as_view(model=Posts,
					template_name='blog/blog_detail.html')
					, name="blog_detail"),



	)