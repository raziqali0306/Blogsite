from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    blog_image = models.ImageField(blank=True, null=True)
    publish_date = models.DateTimeField('publish_date', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_by = models.ManyToManyField(User, related_name='likes')
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:my_blogs")
        
