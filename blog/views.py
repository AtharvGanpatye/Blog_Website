from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView, 
	UpdateView,
	DeleteView
)
from .models import Post


def home(request):
	# Path is to the html file within the templates directory,
	# Django looks for templates directory in our app by default,
	# so we write the path from templates to html file
	
	context = {
		'posts': Post.objects.all() 	# From DataBase, models.py file function Post.
	}
	return render(request, 'blog/home.html', context)


# Class Based View
class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'# <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']		# Ordering Posts from Newest to Oldest.


class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True	
		else:
			return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True	
		else:
			return False


def about(request):
	return render(request, 'blog/about.html', {'title':'About'})

