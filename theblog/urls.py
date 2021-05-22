#from . import  views
from django.urls import path
from .views import AddPostView, HomeView, ArticleDetailView, UpdatePostView, DeletePostView, AddCategoryView

urlpatterns = [
    
    #path('', views.home, name="home"),
    path('', HomeView.as_view() , name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('article/edit_post/<int:pk>', UpdatePostView.as_view(), name= 'edit_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name= 'delete_post'),
    path('add_category/', AddCategoryView.as_view(), name = 'add_category'),
]
