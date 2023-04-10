from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from UserApp.views import UserViewset, UserFollowingViewSet, UserFollow, registration_view,UserDetailViewset

router = routers.DefaultRouter()

router.register('users', UserViewset)
router.register('userfollowings', UserFollowingViewSet, basename='userfollowing')
router.register('userDetail', UserDetailViewset, basename='userDetail')


urlpatterns = [
    path('', include(router.urls)),
    path('follow/<int:pk>/', UserFollow.as_view(), name='follow-user'),
    path('register/', registration_view),

]
