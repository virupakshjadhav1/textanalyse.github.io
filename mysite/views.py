
# i have created this site   viru
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request,  'index.html' )
	#return HttpResponse(""" <a href="https://docs.djangoproject.com/en/3.0/">Django</a>""")


def analyse(request):
	# get the text
	djtext = request.POST.get('text','default')
	removepunc= request.POST.get('removepunc','off')
	uppercase= request.POST.get('uppercase','off')
	lowercase= request.POST.get('lowercase','off')
	countchar= request.POST.get('countchar','off')
	print(djtext)
	#analysed=djtext
	analysed=""
	if removepunc=='on':
		Punctuation="""!()-[],<>./?@#$^&*""''|"""
		
		for char in djtext:
			if char not in Punctuation:
				analysed=analysed+char
		params= {'purpose':'Remove Punctuation' , 'analyse_text':analysed}
		#analyse the text
		return render(request,'analyse.html',params)

	elif(uppercase=='on'):
		for char in djtext:
			analysed=analysed+char.upper()
		params= {'purpose':'UPPERCASE' , 'analyse_text':analysed}
		#analyse the text
		return render(request,'analyse.html',params)



	elif(lowercase=='on'):
		for char in djtext:
			analysed=analysed+char.lower()
		params= {'purpose':'LOWERCASE' , 'analyse_text':analysed}
		#analyse the text
		return render(request,'analyse.html',params)

	elif(countchar=='on'):
		count=0
		for char in djtext:
			if not char==" ":
				count=count+1

			analysed=count
		params= {'purpose':'Count character ' , 'analyse_text':analysed}
		#analyse the text
		return render(request,'analyse.html',params)



	else:
		return HttpResponse("Error")


#def about(request):
#	return HttpResponse("About viru")
#
#
#def contact(request):
#
#	return HttpResponse("<h1>7218328206</h1>")
#
#
#def capitalize(request):
#	# get the text 
#	djtext=(request.GET.get('text','default'))
#	print(djtext)
#	#analyse the text
#	return HttpResponse("""Capitalize the letter " <a href='/'> Back </a>"    """)
#
#def uppercase(request):
#	return HttpResponse("uppercase the letter ")
#
#def lowercase(request):
#	return HttpResponse(""" <h1>Link</h1>     "lowercase the letter " """)
