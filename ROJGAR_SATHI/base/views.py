from django.shortcuts import render,HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

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





def about_view(request):
     return render(request, 'base/about.html')

def privacy_terms_view(request):
    return render(request, 'base/privacy-terms.html')







def login_view(request):
    if request.method == 'POST':
        ...
        user = authenticate(...)
        if user is not None:
            login(request, user)
            if hasattr(user, 'hunarbaazprofile'):
                return redirect('hunarbaaz:hunarbaaz_dashboard')
            elif hasattr(user, 'clientprofile'):
                return redirect('client:client_dashboard')
            else:
                return redirect('home')
