from typing import Any
from django.contrib import admin
from .models import AppointmentModel
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.save()
        if obj.appointment_status=="Running" and obj.appointment_types=="Online":
            email_subject = 'Appointment is Running'
            email_body = render_to_string('appointment_email.html',{'user':obj.patient.user,'doctor':obj.doctor.user})
            email=EmailMultiAlternatives(email_subject,'',to=[obj.patient.user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()

admin.site.register(AppointmentModel,AppointmentAdmin)