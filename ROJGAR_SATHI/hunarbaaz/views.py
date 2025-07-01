from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Hunarbaaz
from .forms import HunarbaazProfileForm, HunarbaazUserForm

# Home page view
def home(request):
    categories = ['Electrician', 'Plumber', 'Technician', 'Construction', 'Painter', 'Welder']
    reviews = [
    {"text": "Amazing service! Got a skilled plumber within minutes.", "name": "Client A", "stars": 4},
    {"text": "Quick and reliable electrician. Fully satisfied!", "name": "Client B", "stars": 5},
    {"text": "Professional and polite workers!", "name": "Client C", "stars": 4},
    {"text": "Very helpful during emergency work.", "name": "Client D", "stars": 5},
]

    return render(request, 'hunarbaaz/home.html', {'categories': categories, 'reviews':reviews})

# Karigar list page
def karigar_list(request):
    return render(request, 'hunarbaaz/karigar_list.html')

# Employer registration page
def employer_register(request):
    return render(request, 'hunarbaaz/employer_register.html')

# Login page view
def login_view(request):
    redirect('dashboard')
    return render(request, 'hunarbaaz/login.html')

def about_view(request):
    return render(request, 'hunarbaaz/about.html')

def privacy_terms_view(request):
    return render(request, 'hunarbaaz/privacy-terms.html')




def home(request):
    return render(request, 'base/home.html')

@login_required
def dashboard(request):
    return render(request, 'base/dashboard.html')


def register_hunarbaaz(request):
    if request.method == 'POST':
        user_form = HunarbaazUserForm(request.POST)
        profile_form = HunarbaazProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = HunarbaazUserForm()
        profile_form = HunarbaazProfileForm()

    return render(request, 'hunarbaaz/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
})

@login_required
def hunarbaaz_dashboard(request):
    user = request.user

    try:
        hunarbaaz = Hunarbaaz.objects.get(user=user)
        name = hunarbaaz.full_name or "User"
        location = hunarbaaz.location or "Not Set"
        skills = [hunarbaaz.skill or "Not Set"]
        aadhaar_verified = hunarbaaz.is_verified
        profile_pic = hunarbaaz.profile_pic.url if hunarbaaz.profile_pic else None
    except Hunarbaaz.DoesNotExist:
        # User has not created a profile yet
        name = None
        location = None
        skills = None
        aadhaar_verified = False
        profile_pic = None

    context = {
        'name': name,
        'location': location,
        'skills': skills,
        'aadhaar_verified': aadhaar_verified,
        'profile_pic': profile_pic,
        'completed_jobs': 0,
        'pending_requests': 0,
        'ongoing_jobs': 0,
        'rating': 0,
        'recent_reviews': [],
    }

    return render(request, 'hunarbaaz/dashboard.html', context)

@login_required
def edit_profile(request):
    try:
        hunarbaaz = Hunarbaaz.objects.get(user=request.user)
    except Hunarbaaz.DoesNotExist:
        return redirect('hunarbaaz:register_hunarbaaz')

    if request.method == 'POST':
        form = HunarbaazProfileForm(request.POST, request.FILES, instance=hunarbaaz)
        if form.is_valid():
            form.save()
            return redirect('hunarbaaz:hunarbaaz_dashboard')
    else:
        form = HunarbaazProfileForm(instance=hunarbaaz)

    return render (request,'hunarbaaz/edit_profile.html',{'form': form})


