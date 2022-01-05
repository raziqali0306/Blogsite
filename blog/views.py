from django import forms
from django.contrib.auth import authenticate, login, logout, models
from django.db import models
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic import ListView, TemplateView, View, UpdateView, CreateView, DeleteView
from . import models, forms
from django.shortcuts import render

# Create your views here.

app_name = 'blog'

# views on ### Navgation bar ### and help function

## 1
class IndexView(ListView):
    model = models.Blog
    queryset = models.Blog.objects.order_by('-publish_date')

## 2
class TopBlogs(ListView):
    model = models.Blog
    queryset = models.Blog.objects.order_by('-likes')

## spl funciton
def LikePost(request, likeId) :
    if request.user.is_authenticated :
        blog_obj = models.Blog.objects.get(id=int(likeId))
        blog_obj.liked_by.add(request.user)
        blog_obj.likes  = blog_obj.liked_by.count()
        blog_obj.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else :
        return HttpResponseRedirect('/login')

## 3
class Announcements(TemplateView) :
    template_name = 'blog/announcements.html'

# Views of DropDown when user is logged out

## 1
class Login(View) :
    form_class = forms.UserForm
    initial = {'key': 'value'}
    template_name = 'blog/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = forms.UserForm
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user : 
            if user.is_active :
                login(request, user)
                return HttpResponseRedirect('/')  

        return render(request, self.template_name, {'form': form})

## 2
class Register(View):
    form_class = forms.UserForm
    initial = {'key': 'value'}
    template_name = 'blog/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/login/')

        return render(request, self.template_name, {'form': form})



# Views of DropDown when user is not logged in

## 1
class MyBlogs(View):
    
    def get(self, request, *args, **kwargs):
        blogs = models.Blog.objects.filter(author=request.user.id).order_by('-publish_date')
        return render(request, 'blog/my_blogs.html', context={'my_blogs' : blogs})

## 2
class Profile(TemplateView):
    template_name = 'blog/profile.html'


## 3
class Logout(View):
    def get(self, request) :
        logout(request)
        return HttpResponseRedirect('/')


# blog class

class CreateBlog(CreateView):
    model = models.Blog
    fields = ['title', 'description', 'blog_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        print(self.request)
        form.save()
        return HttpResponseRedirect('/myBlogs')

class UpdateBlog(UpdateView):
    model = models.Blog
    fields = ['title', 'description', 'blog_image']

class DeleteBlog(DeleteView):
    model = models.Blog
    success_url = reverse_lazy('blog:my_blogs')