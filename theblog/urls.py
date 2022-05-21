from django.urls import path
from theblog.views import CreatePostView, DeletePostView, HomeView, PostView, UpdatePostView, CreateCategoryView


urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('post/<int:pk>',PostView.as_view(),name='post'),
    path('create/',CreatePostView.as_view(),name='create'),
    path('post/update/<int:pk>/',UpdatePostView.as_view(),name='update'),
    path('post/<int:pk>/remove',DeletePostView.as_view(),name='delete'),
    path('create_category/',CreateCategoryView.as_view(),name='create_category')

]