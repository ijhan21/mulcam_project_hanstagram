from django.db import models
from user.models import User
# Create your models here.
class Feed(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_feed') # 글쓴이
    content = models.TextField()    # 글내용
    image = models.TextField()  # 피드 이미지
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='likes_feed')

    def __str__(self):
        return self.content
    class Meta:
        ordering=['-create_date']

class Reply(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_reply') # 글쓴이
    feed_id = models.ForeignKey(Feed,on_delete=models.CASCADE, related_name='feed_reply')
    reply_content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        ordering=['-create_date']

class Bookmark(models.Model):
    feed_id = models.ForeignKey(Feed,on_delete=models.CASCADE, related_name='feed_bookmark')
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_bookmark') # 글쓴이
    is_marked = models.BooleanField(default=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        ordering=['-create_date']
