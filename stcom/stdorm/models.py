from pyexpat import model
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.text import slugify


# Create your models here.


class DormPost(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    caption = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    created = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=200, default="+90134234234234")
    address = models.TextField(max_length=200,default="Istanbul/Turkey")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
