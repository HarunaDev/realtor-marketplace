# accounts/urls.py
from django.urls import path
from .views import signup

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    # You can add more paths for other user-related views here
]
