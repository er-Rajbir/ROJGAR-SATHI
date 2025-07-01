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