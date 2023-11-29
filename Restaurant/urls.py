from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register("booking", BookingViewSet)
router.register("menu", MenuViewSet)

urlpatterns = [
    path("", index, name="index"),
    path("api/", include(router.urls)),
]
