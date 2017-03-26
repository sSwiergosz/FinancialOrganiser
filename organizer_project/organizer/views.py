from django.shortcuts import render

def index(request):
	
	return render(request, 'organizer/index.html')


def home(request):

	return render(request, 'organizer/home.html')
