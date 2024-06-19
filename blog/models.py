from django.db import models
from authentication.models import MyUser


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='post_author')
    image = models.ImageField(upload_to='post_image/')
    description = models.CharField(max_length=500, null=True, blank=True)

    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.author.user.username


class Comment(BaseModel):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='comment_author')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    message = models.CharField(max_length=250)


class LikePost(BaseModel):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='like_author')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_post')


class FollowUser(BaseModel):
    follower = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='following')



