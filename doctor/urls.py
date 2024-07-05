from rest_framework.routers import DefaultRouter
from .views import DesignationView,SpecializationView,DoctorView,AvialableTimeView,ReviewView
from django.urls import path,include

router = DefaultRouter()

router.register('doctor_des',DesignationView)
router.register('doctor_spc',SpecializationView)
router.register('doctor',DoctorView)
router.register('aviable_time',AvialableTimeView)
router.register('review',ReviewView)

urlpatterns = [
    path('',include(router.urls))
]
