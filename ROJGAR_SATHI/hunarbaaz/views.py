from django.shortcuts import render,HttpResponse
from django.shortcuts import render

# Home page view
def home(request):
    return render(request, 'hunarbaaz/home.html')

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
