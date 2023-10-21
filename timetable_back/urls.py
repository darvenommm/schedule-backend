from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', include('timetable_back_app.urls')),
]
