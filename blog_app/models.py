from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

class Blog(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    blog_title=models.CharField(max_length=100,verbose_name='Title')
    slug=models.SlugField(max_length=250,unique=True)
    blog_content=HTMLField(verbose_name='Description')
    blog_image=models.ImageField(upload_to='blog_images',verbose_name='Image')
    publish_date=models.DateField(auto_now_add=True)
    update_date=models.DateField(auto_now=True)
    class Meta:
        ordering=['-publish_date']
    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='blog_comment')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comment')
    comment=models.CharField(max_length=100,verbose_name='')
    comment_date=models.DateField(auto_now_add=True)
    class Meta:
        ordering=['-comment_date']
    def __str__(self):
        return self.comment
