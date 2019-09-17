from django.urls import path, include
from todo.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register('', TodoViewSet)

urlpatterns = [
    path('', include(router.urls))
    ]