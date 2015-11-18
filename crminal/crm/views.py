from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView, View, TemplateView, CreateView, UpdateView, DeleteView 
from django.views.generic.detail import SingleObjectMixin
from django.core.urlresolvers import reverse_lazy, reverse
from django import forms

from .models import Stage, Company, Contact, Campaign, Opportunity, Reminder, Report, CallLog, OpportunityStage 

# Create your views here.
class ContactList(ListView):
	model = Contact

class ContactDetail(DetailView):
	model = Contact
