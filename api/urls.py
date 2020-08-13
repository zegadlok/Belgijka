from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, RoomViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('rooms', RoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
