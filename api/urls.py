from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import SimpleRouter

from .views import ExpositionAPIView

router = SimpleRouter()
router.register('expositions', ExpositionAPIView)

urlpatterns = [
    path('api/', include(router.urls)),
]