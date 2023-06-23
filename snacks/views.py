# from django.shortcuts import render
from django.views.generic import TemplateView , ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Snacks
# from .models import Thing

# Create your views here.
class HomePageView(TemplateView):
    template_name="home.html"

class AboutPageView(TemplateView):
    template_name="about.html"

class SnacksListView(ListView):
    template_name="snacks.html"
    model = Snacks
    context_object_name = 'snacks'

class SnacksDetailsView(DetailView):
    template_name = "snacks_details.html"
    model = Snacks

class SnacksCreateView(CreateView):
    template_name='snacks_create.html'
    model=Snacks
    fields= ['name', 'description', 'purchaser']

class SnacksUpdateView(UpdateView):
    template_name='snacks_update.html'
    model=Snacks
    fields= "__all__" 
    # ['name', 'description', 'purchaser']
    success_url= reverse_lazy('snacks')

class SnacksDeleteView(DeleteView):
    template_name='snacks_delete.html'
    model=Snacks
    success_url= reverse_lazy('snacks')
   