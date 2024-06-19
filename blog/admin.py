from django.contrib import admin
from blog.models import Post, Comment, LikePost, FollowUser

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(LikePost)
admin.site.register(FollowUser)

