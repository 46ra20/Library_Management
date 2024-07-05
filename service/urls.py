from rest_framework.routers import DefaultRouter
from .views import ServiceView
from django.urls import path,include

router = DefaultRouter()
router.register('',ServiceView)

urlpatterns = [
    path('',include(router.urls))
]
