from django.shortcuts import render,HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Home page view
from client.models import PostRequest  # Make sure this import is at the top

def home(request):
    categories = ['Electrician', 'Plumber', 'Technician', 'Construction', 'Painter', 'Welder']

    # ⭐ Get recent completed reviews with rating
    reviews = PostRequest.objects.filter(is_completed=True, review__isnull=False # ✅ 
   ).select_related('client').order_by('-created_at')[:9]  # Change limit as needed

    return render(request, 'base/home.html', {
        'categories': categories,
        'reviews': reviews
    })






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
  


