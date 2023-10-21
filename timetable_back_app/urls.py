from django.urls import path
from . import views
from .views import*

urlpatterns = [
     path('register/', views.register, name='register'),
     path('github/', GithubSocialAuthView.as_view()),
    #  path('logout/', views.LogoutView.as_view(), name ='logout')
]