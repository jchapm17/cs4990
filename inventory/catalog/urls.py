from django.conf.urls import url

from django.views.generic import TemplateView
from . import views

url patterns = [
	url(r'^$', views.CategoryListView.as_view(), name="categorylist"),
	url(r'^category/(?P<category_id>[0-9]+)/$', views.ItemListView.as_view(), name="itemlist"),
	url(r'^category/add/$', views.CreateCategoryView.as_view(), name="addcategory"),
	url(r'^category/(?P<pk>[0-9]+)/$', viewsUpdateCategoryView.as_view(), name="categoryupdate"),
	url(r'^category/(?P<pk>[0-9]+)/delete/$', views.DeleteCategoryView.as_view(), name='deletecategory'),
	url(r'category/delete/success/$', TemplateView.as_view(template_name="catalog/success.html", name="deletesuccess"),
	url(r'^item/add/$', views.CreateItemView.as_view(), name="additem"),
	url(r'^item/(?P<pk>[0-9]+)/$', views.UpdateItemView.as_view(), name="itemupdate"),
	url(r'^item/(?P<pk>[0-9]+)/delete/$', views.DeleteItemView.as_view(), name="deleteitem"),
	url(r'^item/delete/success/$', TemplateView.as_view(template_name="catalog/success.html"), name="deletesuccess"),
]
