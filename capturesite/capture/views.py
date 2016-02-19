from django.shortcuts import render
from django.http import HttpResponse
from .models import Opportunity

global latest_oppportunity_list

def index(request):
	latest_oppportunity_list = Opportunity.objects.order_by('-solicitation_date')[:5]
	output = ', '.join([o.opportunity_name for o in latest_oppportunity_list])
	return HttpResponse(output)



# Create your views here.
def oppdetail(request, opportunity_id):
	return HttpResponse("You're looking at opportunity %s." % opportunity_id)

def oppresults(request, opportunity_id):
	response = "You're looking at the results of opportunity %s."
	return HttpResponse(response % opportunity_id)
