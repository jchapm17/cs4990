from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', (views.AllPostsView.as_view()), name="allposts"),
   url(r'^profile/(?P<pk>[0-9]+)/$', (views.ProfileDetailView.as_view()), name="theirposts"),
]
