# from django.shortcuts import render
from django.views.generic import TemplateView , ListView, DetailView
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

   