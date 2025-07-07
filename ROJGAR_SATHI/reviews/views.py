from django.shortcuts import render, redirect
from .forms import PublicContactForm

def public_contact(request):
    if request.method == 'POST':
        form = PublicContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'reviews/thank_you.html')
    else:
        form = PublicContactForm()
    
    return render(request, 'reviews/contact_review.html', {'form': form})
