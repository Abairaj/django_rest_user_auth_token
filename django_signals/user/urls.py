from django.urls import path,include
from .views import UserCreateAPIView

urlpatterns = [
    path('user_registration/',UserCreateAPIView.as_view(),name='user_registration')
]
