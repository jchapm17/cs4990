from django.shortcuts import render
from django.views import generic
from django.core.context_processors import csrf

from .models import Post, Comment, Category
# Create your views here.
class IndexView(generic.ListView):
	template_name = 'blogapp/index.html'
	model = Post
	
	def get_queryset(self):
		#SELECT * from blogapp_post ORDER BY pub_date DEC LIMIT 5
		return Post.objects.order_by('-pub_date')[:5]

class PostDetailView(generic.DetailView):
	model = Post	

class CategoryDetailView(generic.DetailView):
	model = Category

	# query set


