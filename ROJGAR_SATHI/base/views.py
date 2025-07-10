from django.shortcuts import render,HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("User logged in:", user)

            # Redirect based on profile
            if hasattr(user, 'hunarbaaz'):
                
                return redirect('hunarbaaz:hunarbaaz_dashboard')
            elif hasattr(user, 'clientprofile'):
               
                return redirect('client:client_dashboard')
            else:
               
                return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    else:
        return render(request, 'base/login.html')
    
def access_denied(request):
    return render(request, 'base/access_denied.html')
  


# send email concept

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def send_mail_page(request):
    context = {}

    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "base/index.html", context)