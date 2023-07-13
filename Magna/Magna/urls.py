"""
URL configuration for Magna project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import Auth.views, Data.views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from Auth.forms import PasswordChange, Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Login/', Login.as_view(
            template_name='Auth/Login.html',
            redirect_authenticated_user=True),
        name='login'),
    path('Logout/', LogoutView.as_view(), name='logout'),
    # path('Change-Password/', PasswordChange.as_view(
    #         template_name='Auth/Password_Change_Form.html'),
    #         name='password_change'
    #     ),
    # path('Change-Password-Done/', PasswordChangeDoneView.as_view(
    #         template_name='Auth/Password_Change_Done.html'),
    #         name='password_change_done'
    #     ),
    # path('Reset-Password/', PasswordResetView.as_view(
    #         template_name='Auth/Reset_Password.html'),
    #         name='password_reset'
    #     ),
    # path('Reset-Password/Done/', PasswordResetDoneView.as_view(
    #         template_name='Auth/Reset_Password_Done.html'),
    #         name='password_reset_done'
    #     ),
    # path('Reset-Password/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
    #         template_name='Auth/Reset_Password_Confirm.html'),
    #         name='password_reset_confirm'
    #     ),
    # path('Reset-Password/Complete/', PasswordResetCompleteView.as_view(
    #         template_name='Auth/Reset_Password_Complete.html'),
    #         name='password_reset_complete'
    #     ),
    path('Signup/', Auth.views.signup_page, name='signup'),
    path('<int:id>/', Data.views.topic_view, name='detail'),
    path('', Data.views.Red, name='home'),
    path('Search/', Data.views.Search, name='search'),
    path('Index/', Data.views.Index, name='index'),
]
