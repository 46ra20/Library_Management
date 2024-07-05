from django.db import models
from patient.models import PatientModel
from doctor.models import DoctorModel,AvailableTimeModel
# Create your models here.

APPOINTMENT_STATUS =[
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Running','Running'),
]

APPOINTMENT_TYPES=[
    ('Offline','Offline'),
    ('Online','Online'),
]

class AppointmentModel(models.Model):
    patient = models.ForeignKey(PatientModel,on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorModel,on_delete=models.CASCADE)
    appointment_types = models.CharField(choices=APPOINTMENT_TYPES,max_length=20)
    appointment_status = models.CharField(choices=APPOINTMENT_STATUS,max_length=20)
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTimeModel,on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Doctor : {self.doctor.user.first_name} , Patient : {self.patient.user.first_name}"
