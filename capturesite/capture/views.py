from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Opportunity

global context

def index(request):
	latest_opportunity_list = Opportunity.objects.order_by('-solicitation_date')[:5]
	context = {'latest_opportunity_list': latest_opportunity_list}
	return render(request, 'capture/index.html', context)


# Create your views here.
def oppdetail(request, opportunity_id):
	opportunity = get_object_or_404(Opportunity, pk=opportunity_id)
	return render(request, 'capture/detail.html', {'opportunity': opportunity})

def oppresults(request, opportunity_id):
	response = "You're looking at the results of opportunity %s."
	return HttpResponse(response % opportunity_id)
