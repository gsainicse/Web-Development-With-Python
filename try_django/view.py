from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
	my_title="Hello There... "
	context ={"title":my_title,"my_list":[1,2,3,4,5]}
	#template_name= "title.txt"
	#template_obj =get_template(template_name)
	#rendered_string =template_obj.render(context)

	return render(request, "hello_world.html",context)
	#return render(request,"hello_world.html", {"title": rendered_string})


def about_page(request):
	return render(request,"AboutUs.html", {"title": "About Us"})


def contact_page(request):
	return render(request,"contact_page.html", {"title": "Contact Us"})

def example_page(request):
	context ={"title":"example"}
	template_name= "example_page.html"
	template_obj =get_template(template_name)
	return HttpResponse(template_obj.render(context))