from django.urls import path
from apps.users.views import register, login, account, account_update
from django.contrib.auth import views as auth_views #import this


urlpatterns = [
    path('register/', register, name = "register"),
    path('login/', login, name = "login"),
    path('setting/user/<int:id>', account_update, name = "account_update"),
    path('account/<str:username>', account, name = "account"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),      
]    