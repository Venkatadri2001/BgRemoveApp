from django.db import models

class BackgroundImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='backgrounds/')

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')
    result = models.ImageField(upload_to='results/', null=True, blank=True)
    background = models.ForeignKey(BackgroundImage, on_delete=models.SET_NULL, null=True, blank=True)
