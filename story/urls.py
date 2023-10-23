# articles/urls.py
from django.urls import path
from .views import (
StoryListView,
StoryUpdateView,
StoryDetailView,
StoryDeleteView,
StoryCreateView,
StoryDashboardListView,
)
urlpatterns = [
    path('<int:pk>/edit/',
         StoryUpdateView.as_view(), name='story_edit'),
    path('<int:pk>/',
         StoryDetailView.as_view(), name='story_detail'),
    path('<int:pk>/delete/',
         StoryDeleteView.as_view(), name='story_delete'),
    path('', StoryListView.as_view(), name='story_list'),
    path('create', StoryCreateView.as_view(), name='story_create'),
    path('mystories', StoryDashboardListView.as_view(), name='mystories'),
]