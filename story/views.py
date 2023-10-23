# articles/views.py
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Genre, Story
from .forms import StoryForm
from django.shortcuts import redirect
from django.urls import reverse


# Stories
class StoryListView(LoginRequiredMixin, ListView):
    model = Story
    template_name = 'story/story_list.html'
    login_url = 'login'


class StoryDashboardListView(LoginRequiredMixin, ListView):
    model = Story
    template_name = 'story/story_dashboard_list.html'
    login_url = 'login'

    def get_queryset(self):
        return Story.objects.filter(author=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            # Handle the case when the user hasn't authored any stories
            return redirect(reverse('dashboard'))  # Redirect to a different view

        return super().dispatch(request, *args, **kwargs)


# detail
class StoryDetailView(LoginRequiredMixin, DetailView):
    model = Story
    template_name = 'story/story_detail.html'
    login_url = 'login'

class StoryCreateView(LoginRequiredMixin, CreateView):
    form_class = StoryForm
    model = Story
    template_name = 'story/story_new.html'
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class StoryUpdateView(LoginRequiredMixin, UpdateView):
    form_class = StoryForm
    model = Story
    template_name = 'story/story_edit.html'
    login_url = 'login'
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class StoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Story
    template_name = 'story/story_delete.html'
    success_url = reverse_lazy('mystories')
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

# Genres
# list
class GenreListView(LoginRequiredMixin, ListView): # new
    model = Genre
    template_name = 'genre_list.html'
    login_url = 'login' # new

# detail
class GenreDetailView(LoginRequiredMixin, DetailView):
    model = Genre
    template_name = 'genre_detail.html'
    login_url = 'login'

