from django.db import models

# Create your models here.
class ServiceModel(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    images = models.ImageField(upload_to='service/image')