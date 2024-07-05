from django.db import models
from django.contrib.auth.models import User
from patient.models import PatientModel
# Create your models here.
STAR_CHOICES = [
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
    
]

class SpecializationModel(models.Model):
    name=models.CharField(max_length=30)
    slug=models.SlugField(max_length=30)

    def __str__(self):
        return self.name

class DesignationsModel(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class AvailableTimeModel(models.Model):
    available_time= models.CharField(max_length=100)

    def __str__(self):
        return self.available_time

class DoctorModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField( upload_to='doctor/images/')
    designation = models.ManyToManyField(DesignationsModel)
    specialization = models.ManyToManyField(SpecializationModel)
    available_time = models.ManyToManyField(AvailableTimeModel)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"



class ReviewModel(models.Model):
    reviewer  = models.ForeignKey(PatientModel,on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=10,choices=STAR_CHOICES)

    def __str__(self) -> str:
        return f'Reviewer: {self.reviewer.user.first_name} to Doctor: {self.doctor.user.first_name}'