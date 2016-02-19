from django.conf.urls import url
from capture import views


urlpatterns = [ url(r'^$', views.index, name='index'), 
		url(r'^(?P<opportunity_id>\d+)$', views.oppdetail, name = 'oppdetail'),
		url(r'^(?P<opportunity_id>\d+)/results', views.oppresults, name='oppresults'),
	]
