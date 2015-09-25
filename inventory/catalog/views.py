from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from modles import Item, Category

# Create your views here.
class CategoryListView(ListView):
	model = Category

class CreateCategoryView(CreateView):
	model = Category
	fields = ['name', 'descriptiom']
	success_url = reverse_lazy('inventory:categorylist')

class UdateCategoryView(UpdateView):
	model = Category
	fields = ['name', 'description']

class DeleteCategoryView(DeleteView):
	model = Category

class ItemListView(ListView):
	model = Item

class CreateItemView(CreateView):
	model = Item
	fields = ['name', 'quantity', 'sku', 'category']
	

class UpdateItemView(updateView):
	model = Item
        fields = ['name', 'quantity', 'sku', 'category']
        
class DeleteItemView(DeleteView):
	model = Item
