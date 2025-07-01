from django.shortcuts import render,HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Home page view
def home(request):
    categories = ['Electrician', 'Plumber', 'Technician', 'Construction', 'Painter', 'Welder']
    reviews = [
    {"text": "Amazing service! Got a skilled plumber within minutes.", "name": "Client A", "stars": 4},
    {"text": "Quick and reliable electrician. Fully satisfied!", "name": "Client B", "stars": 5},
    {"text": "Professional and polite workers!", "name": "Client C", "stars": 4},
    {"text": "Very helpful during emergency work.", "name": "Client D", "stars": 5},
]

    return render(request, 'base/home.html', {'categories': categories, 'reviews':reviews})

# Karigar list page


# Employer registration page


# Login page view
def login_view(request):
    return render(request, 'base/login.html')

def about_view(request):
    return render(request, 'base/about.html')

def privacy_terms_view(request):
    return render(request, 'base/privacy-terms.html')




def home(request):
    return render(request, 'base/home.html')

@login_required
def dashboard(request):
    return render(request, 'hunarbaaz/dashboard.html')
#@login_required
#def edit_profile(request):
 #   return render (request,'hunarbaaz/edit_profile.html')