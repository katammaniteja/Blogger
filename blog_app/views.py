from django.forms import fields
from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import CreateView,UpdateView,ListView,DetailView,TemplateView,ListView
from .models import Comment,Blog
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import re
from django.contrib import messages

# Create your views here.
@login_required
def MyBlogs(request):
    return render(request,'user_blogs.html')

class UpdateBlog(LoginRequiredMixin,UpdateView):
    context_object_name='blogs'
    model=Blog
    template_name='edit_blog.html'
    fields=('blog_title','blog_content','blog_image')
    def get_success_url(self,**kwargs):
        return reverse_lazy('blog_app:blog_details',kwargs={'slug':self.object.slug})

class blog_list(ListView):
    model=Blog
    context_object_name='blogs'
    paginate_by=3
    template_name="blog_list.html"

class create_blog(LoginRequiredMixin,CreateView):
    model=Blog
    template_name='create_blog.html'
    fields=('blog_title','blog_content','blog_image')
    def form_valid(self,form):
        blog_obj=form.save(commit=False)
        blog_obj.author=self.request.user
        title=blog_obj.blog_title
        title=title.strip();
        title=re.sub('[^a-zA-z ]','',title);
        blog_obj.slug=title.replace(' ','-')+ "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))
 
def blog_details(request,slug):
    blog=Blog.objects.get(slug=slug)
    if request.method=='POST':
        if not blog.author==request.user:
            comment=request.POST.get('comment')
            new_comment=Comment.objects.create(comment=comment,blog=blog,user=request.user)
            new_comment.save()
            return HttpResponseRedirect(reverse('blog_app:blog_details',kwargs={'slug':slug}))
        else:
            messages.info(request,"You cannot comment on your blog")
            return render(request,'blog_details.html',context={'blog':blog})

@login_required
def DeleteBlog(request,pk):
    blog=Blog.objects.get(pk=pk).delete()
    return HttpResponseRedirect(reverse('blog_app:my_blogs'))