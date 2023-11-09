from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.ImageField(upload_to='food_pictures', default='defaultfood.jpg',)
    item_address = models.CharField(max_length=500,default="Istanbul/Turkey")


    def __str__(self):
        return self.item_name


    def get_absolute_url(self):
        return reverse("stfood:detail", kwargs={"pk": self.pk})



