from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from .validators import file_size
from ckeditor.fields import RichTextField
from tagify.models import TagField

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, default='New Post')
    price = models.FloatField("post price", default='15')
    description = RichTextField(blank=True,max_length=255)
    # description = models.TextField(max_length=255, blank=False)
    pic = models.ImageField(upload_to='path/to/img', blank=False)
    video = models.FileField(upload_to='videos/', validators=[file_size], blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TagField(verbose_name='tags',max_length=100, blank=False,default='Other')
    # tags = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=255, blank=False, default='Other')
    targetlocation = models.CharField(max_length=255, blank=False, default='Other')


    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    @property
    def get_pic_url(self):
        if self.pic and hasattr(self.pic, 'url'):
            return self.pic.url
        else:
            return "/static/images/user.jpg"




class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
    username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    comment_date = models.DateTimeField(default=timezone.now)


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
