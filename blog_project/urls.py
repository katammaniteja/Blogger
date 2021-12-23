from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('users_app.urls')),
    path('blog/',include('blog_app.urls')),
    path('',views.home,name='index'),
    path('oauth/', include('social_django.urls', namespace='social')),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)