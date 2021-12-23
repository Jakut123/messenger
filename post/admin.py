from django.contrib import admin



# Register your models here.
from post.models import Post, Tag, Comment

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
