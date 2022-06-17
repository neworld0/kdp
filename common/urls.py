from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# from django.conf.urls import url


app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('password_reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('change_password/', views.change_password, name='change_password'),
    # path('password_change/', views.MyPasswordChangeView.as_view(), name='password_change'),
]