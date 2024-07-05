from django.db import models

# Create your models here.
class ContactUsModel(models.Model):
    name=models.CharField(max_length=40)
    phone = models.CharField(max_length=13)
    problem = models.TextField()

    def __str__(self):
        return self.name
    