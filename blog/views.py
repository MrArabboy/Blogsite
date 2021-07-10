from blog.forms import BlogCreateForm
from django.shortcuts import render, resolve_url
from .models import Blog
from django.views.generic import ListView,CreateView
from .forms import BlogCreateForm

    
class BlogListView(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        users = self.request.user
        blogs = Blog.objects.filter(title='Blog1')
        return blogs

class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog/blog_create.html'
    form_class = BlogCreateForm
   

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
