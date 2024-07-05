from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PatientView,UserRegistrationView,activate,UserLoginView,UserLogoutView
router = DefaultRouter()
router.register("",PatientView)
# router.register("register/",UserRegistrationView)

urlpatterns = [
    path("patient_view/",include(router.urls)),
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('active/<uid64>/<token>/',activate),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout')
]
