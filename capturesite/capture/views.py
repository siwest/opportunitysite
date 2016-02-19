from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, You're at the capture opportunity site.")
# Create your views here.
def oppdetail(request, opportunity_id):
	return HttpResponse("You're looking at opportunity %s." % opportunity_id)

def oppresults(request, opportunity_id):
	response = "You're looking at the results of opportunity %s."
	return HttpResponse(response % opportunity_id)
