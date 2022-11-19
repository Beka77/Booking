from django.urls import path
from apps.users.views import register, login, account, account_update
from django.contrib.auth import views as auth_views #import this
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register, name = "register"),
    path('login/', login, name = "login"),
    path('setting/user/<str:username>', account_update, name = "account_update"),
    path('account/<str:username>', account, name = "account"),
    path('logout/', LogoutView.as_view(next_page = 'index'), name = "logout"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),      
]    