from django.shortcuts import render,HttpResponse
from django.shortcuts import render

# Home page view
def home(request):
    categories = ['Electrician', 'Plumber', 'Technician', 'Construction', 'Painter', 'Welder']
    return render(request, 'home.html', {'categories': categories})

# Karigar list page
def karigar_list(request):
    return render(request, 'hunarbaaz/karigar_list.html')

# Employer registration page
def employer_register(request):
    return render(request, 'hunarbaaz/employer_register.html')

# Login page view
def login_view(request):
    return render(request, 'hunarbaaz/login.html')
# Create your views here.
