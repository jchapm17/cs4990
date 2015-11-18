from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views
from .views import *
from .models import *

urlpatterns = [
   url(r'^contact/$', views.ContactList.as_view(), name="contactlist"),
   url(r'^contact/(?P<pk>[0-9]+)/$', views.ContactDetail.as_view(), name="contactdetail"),
]
