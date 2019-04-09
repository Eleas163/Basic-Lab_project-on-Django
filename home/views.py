from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
	#return HttpResponse('<h1>welcome<h1/>')
	return render(request, 'index.html')