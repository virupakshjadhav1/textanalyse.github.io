# this is inside 

from django.http import HttpResponse

def i_am_inside(request):
	return HttpResponse("I am inside ")