from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from UserApp.views import CustomAuthToken
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('uapi/',include('UserApp.urls')),
    path('auth/',CustomAuthToken.as_view(), name='auth-user'),
    path('papi/',include('PostApp.urls')),
    path('profile/',include('ProfileApp.urls')),
    path('',include('UiApp.urls'))
]