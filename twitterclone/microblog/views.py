from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView, View, TemplateView, CreateView, UpdateView 
from django.views.generic.detail import SingleObjectMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django import forms

from .models import Profile, Post

# Create your views here.
class ListAllPosts(ListView):
    model = Post
    paginate_by = 10
    queryset = Post.objects.all().order_by('-pub_date')

class ProfileDetailView(DetailView):
    model = Profile

class MyFeedView(ListView):
    model = Post
    paginate_by = 10
    template_name = "microblog/myfeed.html"

    def get_queryset(self):
        #my_profile = self.request.user.profile_set.all()[0]
	my_profile, created = Profile.objects.get_or_create(user = self.request.user)
        following_profile_list = list(my_profile.following.all())
        following_profile_list.append(my_profile)
        return Post.objects.filter(profile__in = following_profile_list)

class FollowFormView(SingleObjectMixin, View):
    model = Profile

    def post(self, request, *args, **kwargs):
	try:
		my_profile = request.user.profile_setall()[0]
        except Profile.DoesNotExist:
		my_proile = Profile(bio = '', user = request.user)
        	my_profile.save()
	my_profile.following.add(self.get_object())
	my_profile.save()
        #return HttpResponseRedirect(reverse('microblog:followsuccess', kwargs = {'pk': self.get_object().pk}))
        #if request.is_ajax():
         #   return Http
        return HttpResponseRedirect(reverse('microblog:followsuccess', args = (self.get_object().pk,)))

class FollowSuccessView(DetailView):
    template_name = 'microblog/follow_success.html'
    model = Profile

class CreatePostView(CreateView):
    model = Post
    fields = ['body']

    def get_success_url(self):
        return reverse('microblog:myfeed')

    def form_valid(self, form):
        u = form.save(commit=False)
        u.profile, created = Profile.objects.get_or_create(user=self.request.user)
        u.save()
        return super(CreatePostView, self).form_valid(form)

class CreateProfileView(CreateView):
	model = Profile
	fields = ['bio', 'profile_picture', 'following']

	def get_success_url(self):
		return reverse('microblog:profiledetail', args = (self.request.user.id, ))

	def form_valid(self, form):
		profile = Profile()
		profile.bio = form.cleaned_data['bio']
		profile.profile_picture = form.cleaned_data['profile_picture']
		profile.following = form.cleaned_data['following']
		profile.save()

		return super(CreateProfileView, self).form_valid(form)

class UpdateProfileView(UpdateView):
	model = Profile
	fields = ['bio', 'profile_picture', 'following']

	def get_success_url(self):
		return reverse('microblog:profiledetail', args = (self.get_object().pk,))
