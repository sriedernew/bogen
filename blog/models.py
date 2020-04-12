from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    app_label = 'blog'
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE, related_name='categories')
    tag = models.TextField()
    title = models.CharField(max_length=300)
    text = models.TextField()
    img_url = models.CharField(max_length=1024,blank=True)
    img_alt = models.CharField(max_length=200,blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Category(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name