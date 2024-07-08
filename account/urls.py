from django.urls import path
from account.views import UserCreate
urlpatterns = [
    path('register/', UserCreate.as_view(), name='register')
]
