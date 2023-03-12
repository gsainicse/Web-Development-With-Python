from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
	my_title="Hello There... "
	#return render(request, "hello_world.html")
	return render(request,"hello_world.html", {"title": my_title})


def about_page(request):
	return HttpResponse("<h1> About Us</h1>")


def contact_page(request):
	return HttpResponse("<h1> Contact us </h1>")