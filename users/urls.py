from django.urls import path, include
from . import views


# from rest_framework.routers import DefaultRouter
# from .views import UserCreate
# from .models import User

urlpatterns = [
    
    path('', views.UserCreate.as_view()),
    #path('register/', user.UserCreate.as_view()),
    path('<int:pk>', views.UserDetail.as_view())
]
