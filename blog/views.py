from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
	# Path is to the html file within the templates directory,
	# Django looks for templates directory in our app by default,
	# so we write the path from templates to html file
	
	context = {
		'posts': Post.objects.all() 
		# From DataBase, models.py file function Post.
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})

