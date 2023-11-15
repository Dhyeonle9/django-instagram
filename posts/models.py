from django.db import models
from django_resized import ResizedImageField
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def time_since_created(self):
        time_difference = timezone.now() - self.created_at
        days = time_difference.days
        hours, remainder = divmod(time_difference.seconds, 3600)
        minutes = remainder // 60
        if days >= 1:
            return '{}일'.format(days)
        elif hours >= 1:
            return '{}시간'.format(hours)
        else:
            return " {}분".format(minutes)

    updated_at = models.DateTimeField(auto_now=True)
 
    # image = ImageField(upload_to='image/%Y/%m')
    image = ResizedImageField(
        size=[500, 500], 
        crop=['middle', 'center'], 
        upload_to='image/%Y/%m',
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='child_comments')
    # child_comments