from django.shortcuts import render, redirect
from .forms import ClientRegisterForm
from .models import ClientProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from django.contrib.auth import login




@login_required
def client_dashboard(request):
    profile = ClientProfile.objects.get(user=request.user)
    return render(request, 'client/dashboard_client.html', {'profile': profile})









# def register_view(request):
#     if request.method == 'POST':
#         form = ClientRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(user.password)
#             user.save()
#             login(request, user)
#             return redirect('client:client_dashboard')
#     else:
#         form = ClientRegisterForm()
#     return render(request, 'client/register.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import ClientRegisterForm
from django.contrib.auth import login

def register_view(request):
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)  # log them in
            return redirect('home')  # ⬅️ FIXED: redirect to a working view
    else:
        form = ClientRegisterForm()

    return render(request, 'client/register.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'client/dashboard_client.html')