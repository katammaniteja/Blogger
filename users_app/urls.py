from django.conf.urls import url
from django.urls import path

from blog_project.settings import MEDIA_ROOT
from . import views


app_name='users_app'
urlpatterns = [
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
]


