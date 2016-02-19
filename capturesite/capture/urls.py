from django.conf.urls import url
from . import views

urlpatterns = [ url(r'^$', views.index, name='index'), 
		url(r'^(P<opportunity_id>[0-9]+)/$', views.oppdetail, name = 'oppdetail'),
		url(r'^(P<opportunity_id>[0-9]+)/results', views.oppresults, name='oppresults'),
	]
