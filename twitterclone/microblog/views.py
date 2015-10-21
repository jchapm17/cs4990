from django.shortcuts import render
from .models import Profile, Post
from django.views.generic import ListView, DetailView

# Create your views here.
class AllPostsView(ListView):
	model = Post
	template_name = 'microblog/all_posts.html'
	paginate_by = 1

	def get_queryset(self):
        	return Post.objects.order_by('-pub_date')

class ProfileDetailView(DetailView):
	model = Profile
	template_name = 'microblog/their_posts.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ProfileDetailView,self).get_context_data()
		context['posts'] = Profile.objects.order_by('-pub_date')[:10]
		return context

