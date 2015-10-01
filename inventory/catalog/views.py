from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Item, Category

# Create your views here.
class CategoryListView(ListView):
	model = Category

class CategoryDetailView(DetailView):
	model = Category

class CreateCategoryView(CreateView):
	model = Category
	fields = ['parent', 'name', 'description']
	
	def get_success_url(self):
		return reverse('catalog:categorydetail', args=(self.object.pk,))

class UpdateCategoryView(UpdateView):
	model = Category
	fields = ['parent', 'name', 'description']

	def get_success_url(self):
                return reverse('catalog:categorydetail', args=(self.object.pk,))


class DeleteCategoryView(DeleteView):
	model = Category
	success_url = reverse_lazy('catalog:deletecategorysuccess')

class CreateItemView(CreateView):
	model = Item
	fields = ['name', 'quantity', 'sku', 'category']
	
	def get_success_url(self):
		return reverse('catalog:categorydetail', ars=(self.object.category.id,))	

class UpdateItemView(UpdateView):
	model = Item
        fields = ['name', 'quantity', 'sku', 'category']

	def get_success_url(self):
        	return reverse('catalog:categorydetail', args=(self.object.category.id,))
class DeleteItemView(DeleteView):
	model = Item
	success_url=reverse_lazy('catalog:deleteitemsuccess')
