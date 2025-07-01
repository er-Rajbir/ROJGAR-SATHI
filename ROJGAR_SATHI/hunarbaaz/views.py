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
    hunarbaaz = get_object_or_404(Hunarbaaz, user=user)

    context = {
        'name': hunarbaaz.full_name,
        'location': hunarbaaz.location,
        'skills': [hunarbaaz.skill],  # you can make this a ManyToMany if needed later
        'aadhaar_verified': hunarbaaz.is_verified,
        'profile_pic': hunarbaaz.profile_pic.url if hunarbaaz.profile_pic else None,
        'completed_jobs': 0,  # Replace with actual logic later
        'pending_requests': 0,  # Replace with actual logic later
        'ongoing_jobs': 0,  # Replace with actual logic later
        'rating': 4.2,  # Temporary static value; can link later
        'recent_reviews': [
            {'client': 'Gurpreet', 'text': 'Very professional and skilled'},
            {'client': 'Harpreet', 'text': 'Quick and clean job done'},
        ]
    }

    return render(request, 'hunarbaaz/dashboard.html',context)
@login_required
def edit_profile(request):
    return render (request,'hunarbaaz/edit_profile.html')


