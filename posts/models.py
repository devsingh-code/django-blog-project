from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
# Create your models here.

class User(AbstractUser):
    '''AbstractUser is used as we have directly used all-auth and this user
    has all the methods available as sign in , signup, register'''
    pass

    def __str__(self):
        return self.username



class Post(models.Model):
    '''This handles the posts display on the home page and
    other details related to it'''
    title=models.CharField(max_length=100)
    content=models.TextField()
    thumbnail=models.ImageField()
    publish_date= models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    slug =models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail",kwargs={
            "slug":self.slug
        })

    def get_like_url(self):
        return reverse("like",kwargs={
            "slug":self.slug
        })

    @property    
    def comments(self):
        return self.comment_set.all()

    @property
    def get_comment_count(self):
        return self.comment_set.all().count()


    @property
    def get_view_count(self):
        return self.postview_set.all().count()

    @property
    def get_like_count(self):
        return self.like_set.all().count()


class Comment(models.Model):
    '''It handles the comment section of the Blog'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(Post,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content=models.TextField()

    def __str__(self):
        return self.user.username

class PostView(models.Model):
    '''This handles the detail view of the Posts
    once the user clicks on any blog to read'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username

class Like(models.Model):
    '''This handles the likes for the posts'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
