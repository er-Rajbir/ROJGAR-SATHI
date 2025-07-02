from django.shortcuts import render, redirect
from .forms import ClientRegisterForm
from .models import ClientProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import ClientProfile
from .forms import ClientRegisterForm, ClientProfileForm, UserUpdateForm, PostRequestForm
from django.contrib.auth import login




@login_required
def client_dashboard(request):
    profile = ClientProfile.objects.get(user=request.user)
    return render(request, 'client/dashboard_client.html', {'profile': profile})

@login_required
def edit_profile(request):
    return render(request, 'client/edit_profile.html')




from django.shortcuts import render, redirect
from .forms import ClientRegisterForm, ClientProfileForm
from django.contrib.auth.models import User
from .models import ClientProfile
from django.contrib.auth import login

def register_view(request):
    if request.method == 'POST':
        user_form = ClientRegisterForm(request.POST)
        profile_form = ClientProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('client:client_dashboard')

    else:
        user_form = ClientRegisterForm()
        profile_form = ClientProfileForm()

    return render(request, 'client/client_register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })





@login_required
def edit_profile(request):
    user = request.user
    try:
        profile = user.clientprofile
    except ClientProfile.DoesNotExist:
        profile = ClientProfile.objects.create(user=user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ClientProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('client:client_dashboard')  # Change as per your dashboard path name
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ClientProfileForm(instance=profile)

    return render(request, 'client/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def create_work_request(request):
    if request.method == 'POST':
        form = PostRequestForm(request.POST)
        if form.is_valid():
            work_request = form.save(commit=False)
            work_request.client = request.user
            work_request.save()
            return redirect('client:client_dashboard')  # update this to your actual dashboard URL name
    else:
        form = PostRequestForm()
    return render(request, 'client/post_request.html', {'form': form})