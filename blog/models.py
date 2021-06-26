from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Article(models.Model):
    STATUS = (
        ('draft','Draft'),
        ('publish','Publish')
    )
    title = models.CharField(max_length = 120)
    slug = models.SlugField(max_length = 150, unique = True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    body = RichTextUploadingField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 50 , choices=STATUS, default= 'draft')

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('blog:article_detail',args=[self.id,self.slug])
    