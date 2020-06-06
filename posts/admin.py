from django.contrib import admin
from .models import Post,PostView,Comment,Like,User

# Register your models here.
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(User)
