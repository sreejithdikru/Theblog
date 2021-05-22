from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import DeleteView
from .models import Post, Category
from .forms import EditForm, PostForm
from django.urls import reverse_lazy
#def home(request):
 #   return render(request, 'home.html', {})
class HomeView(ListView):
     model = Post
     template_name = 'home.html'
     ordering = ['-post_date']

class ArticleDetailView(DetailView):
     model = Post
     template_name = 'article_details.html'

class AddPostView(CreateView):
     model = Post
     form_class = PostForm
     template_name = 'add_post.html'
     #fields = '__all__'


class AddCategoryView(CreateView):
     model = Category
     template_name = 'add_category.html'
     fields = '__all__'    

class UpdatePostView(UpdateView):
     model = Post
     form_class = EditForm
     template_name = 'update_post.html'

class DeletePostView(DeleteView):
     model = Post
     template_name = 'delete_post.html'
     success_url = reverse_lazy('home')