from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PatientModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='patient/images/')
    mobail_no = models.CharField(max_length=12)

    def __srt__(self):
        return self.user.user.first_name
