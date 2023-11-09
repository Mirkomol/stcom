from django.db import models


class ProfileCV(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=200)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    work_experience = models.TextField(max_length=200)
    skills = models.TextField(max_length=200)


    def __str__(self):
        return self.name