from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from . import forms
from django.conf import settings
from django.views.generic import View
from django.contrib.auth.decorators import login_required


def logout_user(request):
    logout(request)
    return redirect('login')

# class LoginPageView(View):
#     template_name = 'Auth/Login.html'
#     form_class = forms.LoginForm
    
#     def get(self, request):
#         form = self.form_class()
#         message = ''
#         return render(request, self.template_name, context={'form': form, 'message': message})
        
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         message = 'Login failed!'
#         return render(request, self.template_name, context={'form': form, 'message': message})

@login_required
def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            previous_url = request.session.pop('previous_url', None)
            if previous_url:
                return previous_url
            else:
                return redirect(settings.LOGIN_REDIRECT_URL)
        
    if 'previous_url' not in request.session:
        previous_url = request.META.get('HTTP_REFERER')
        request.session['previous_url'] = previous_url
    return render(request, 'Auth/Signup.html', context={'form': form})