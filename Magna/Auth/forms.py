from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect


class SignupForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class PasswordChange(PasswordChangeView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'previous_url' not in self.request.session:
            previous_url = self.request.META.get('HTTP_REFERER')
            self.request.session['previous_url'] = previous_url
        return context

    def get_success_url(self):
        previous_url = self.request.session.pop('previous_url', None)
        if previous_url:
            return previous_url
        else:
            return reverse_lazy('password_change_done')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Password changed successfully!")
        return response


class Login(LoginView):
    def get(self, request, *args, **kwargs):
        if 'previous_url' not in self.request.session:
            previous_url = self.request.META.get('HTTP_REFERER')
            self.request.session['previous_url'] = previous_url
        print(self.request.session['previous_url'])
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        previous_url = self.request.session.pop('previous_url', None)
        if previous_url:
            return previous_url
        else:
            return reverse_lazy('red')
    
class Logout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        # Perform logout actions
        response = super().dispatch(request, *args, **kwargs)

        # Add logout done message
        messages.success(request, "You have been logged out successfully.")

        # Redirect to a specific URL after logout
        return redirect('home')  # Replace 'home' with your desired URL name or path
