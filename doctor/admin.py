from django.contrib import admin
from .models import SpecializationModel,DesignationsModel,DoctorModel,ReviewModel,AvailableTimeModel

# Register your models here.
class AutoSlugSpecialization(admin.ModelAdmin):
    prepopulated_fields={"slug":["name"]}

admin.site.register(SpecializationModel,AutoSlugSpecialization)
class AutoSlugDesignation(admin.ModelAdmin):
    prepopulated_fields={"slug":["name"]}
    
admin.site.register(DesignationsModel,AutoSlugDesignation)
admin.site.register(DoctorModel)
admin.site.register(AvailableTimeModel)
admin.site.register(ReviewModel)
