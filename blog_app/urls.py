from django.urls import path
from blog_app import views

app_name='blog_app'

urlpatterns = [
    path('',views.blog_list,name='blog_list'),
    path('write-blog/',views.create_blog.as_view(),name='create_blog'),
    path('blog-details/<slug:slug>',views.blog_details,name='blog_details'),
    path('my-blogs/',views.MyBlogs,name='my_blogs'),
    path('edit-blog/<pk>',views.UpdateBlog.as_view(),name='edit_blog'),
    path('delete-blog/<pk>',views.DeleteBlog,name='delete_blog'),
]
