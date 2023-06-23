from django.urls import path 
from .views import HomePageView, AboutPageView , SnacksListView, SnacksDetailsView, SnacksCreateView, SnacksUpdateView, SnacksDeleteView
urlpatterns = [
    path('',HomePageView.as_view(), name="home"),
    path('about',AboutPageView.as_view(), name="about"),
    path('snacks',SnacksListView.as_view(), name="snacks"),
    path('<int:pk>/',SnacksDetailsView.as_view(), name="snacks_details"),
    path('create/',SnacksCreateView.as_view(), name="snacks_create"),
    path('update/<int:pk>',SnacksUpdateView.as_view(), name="snacks_update"),
    path('delete/<int:pk>',SnacksDeleteView.as_view(), name="snacks_delete"),
]