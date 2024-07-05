from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ContactUsViews
router = DefaultRouter()
router.register('',ContactUsViews)

urlpatterns = [
    path('',include(router.urls))
]
