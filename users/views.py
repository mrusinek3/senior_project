import re
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# function based view that displays a form that users use to register an account on the application
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Thank you for creating an {username}, now please Login!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
        'title': 'Register',
    }

    return render(request, 'users/register.html', context)

# function based view that displays a profile page with the all the users information and a form filled with their information for them to update
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your Account Has Been Updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile) 

    context = {
        'title': 'Profile',
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'users/profile.html', context)


