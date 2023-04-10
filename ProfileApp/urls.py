from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from ProfileApp.views import ProfileViewSet, SkillViewSet, AboutViewSet

router = routers.DefaultRouter()
router.register('user_profile', ProfileViewSet)
router.register('skills',SkillViewSet)
router.register('about',AboutViewSet)

urlpatterns = [
    path('', include(router.urls))]
