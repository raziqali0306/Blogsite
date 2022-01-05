from django.urls import re_path
from blog import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^topBlogs/$', views.TopBlogs.as_view(), name='topBlogs'),
    re_path(r'^announcements/$', views.Announcements.as_view(), name='announcements'),
    re_path(r'^login/$', views.Login.as_view(), name='login'),
    re_path(r'^register/$', views.Register.as_view(), name='register'),
    re_path(r'^logout/$', views.Logout.as_view(), name='logout'),
    re_path(r'^likePost/(?P<likeId>[0-9]+)$', views.LikePost, name='likePost'),
    re_path(r'^profile/$', views.Profile.as_view(), name='profile'),
    re_path(r'^myBlogs/$', views.MyBlogs.as_view(), name='my_blogs'),
    re_path(r'^create/$', views.CreateBlog.as_view(), name='createBlog'),
    re_path(r'^edit/(?P<pk>[0-9]+)$', views.UpdateBlog.as_view(), name='updateBlog'),
    re_path(r'^delete/(?P<pk>[0-9]+)$', views.DeleteBlog.as_view(), name='deleteBlog'),
]


