from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_view, name='logout'),  # Ensure the logout_view exists in views.py
    path('password_change/', 
         auth_views.PasswordChangeView.as_view(
             template_name='core/password_change.html',
             success_url=reverse_lazy('core:password_change_done')
         ), 
         name='password_change'),
    path('password_change_done/', 
         auth_views.PasswordChangeDoneView.as_view(template_name='core/password_change_done.html'), 
         name='password_change_done')
]
