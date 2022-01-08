from django.urls import re_path
from blog import views

urlpatterns = [
    re_path(r'^$', views.BlogsView.as_view(), name='index'),
    re_path(r'^topBlogs/$', views.TopBlogsView.as_view(), name='topBlogs'),
    re_path(r'^announcements/$', views.AnnouncementsView.as_view(), name='announcements'),
    re_path(r'^login/$', views.LoginView.as_view(), name='login'),
    re_path(r'^register/$', views.RegisterView.as_view(), name='register'),
    re_path(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    re_path(r'^likePost/(?P<likeId>[0-9]+)$', views.LikePost, name='likePost'),
    re_path(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    re_path(r'^myBlogs/$', views.MyBlogsView.as_view(), name='my_blogs'),
    re_path(r'^create/$', views.CreateBlogView.as_view(), name='createBlog'),
    re_path(r'^edit/(?P<pk>[0-9]+)$', views.UpdateBlogView.as_view(), name='updateBlog'),
    re_path(r'^delete/(?P<pk>[0-9]+)$', views.DeleteBlogView.as_view(), name='deleteBlog'),
]


