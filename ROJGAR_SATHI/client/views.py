from django.shortcuts import render, redirect,get_object_or_404
from django.http import Http404
from .models import ClientProfile,Hunarbaaz, PostRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ClientRegisterForm, ClientProfileForm, UserUpdateForm, PostRequestForm, RescheduleRequestForm, ReviewForm
from django.contrib import messages
#for email
from django.core.mail import send_mail
from django.conf import settings



@login_required
def client_dashboard(request):
    profile = ClientProfile.objects.get(user=request.user)
    return render(request, 'client/dashboard_client.html', {'profile': profile})

@login_required
def edit_profile(request):
    return render(request, 'client/edit_profile.html')

def register_view(request):
    if request.method == 'POST':
        user_form = ClientRegisterForm(request.POST)
        profile_form = ClientProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
              # ✅ Send Email
            
            send_mail(
    subject="🎉 Welcome to Rozgaar Saathi!",
    message=f"""
Hi {profile.full_name},

Thank you for signing up as a Client on Rozgaar Saathi!

Your account details
────────────────────
• Username : {user.username}
• Email    : {user.email}

What you can do next
────────────────────
1. Post a work request and connect with verified Hunarbaaz in your area.
2. Track job status and communicate directly from your dashboard.
3. Rate and review workers after the job is complete to help the community grow.

Need help?
──────────
If you have any questions, simply reply to this e‑mail or call us at +91‑98765‑4XXXX.
Our support team is available Monday–Saturday, 9 am – 6 pm IST.

Welcome aboard!
The Rozgaar Saathi Team
""",
    from_email=settings.DEFAULT_FROM_EMAIL,
    recipient_list=[user.email],
    fail_silently=False,
)
            
            return redirect('base:login')

    else:
        user_form = ClientRegisterForm()
        profile_form = ClientProfileForm()

    return render(request, 'client/client_register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def edit_profile(request):
    user = request.user
    try:
        profile = user.clientprofile
    except ClientProfile.DoesNotExist:
        profile = ClientProfile.objects.create(user=user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ClientProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('client:client_dashboard')  
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ClientProfileForm(instance=profile)

    return render(request, 'client/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })



def hunarbaaz_list(request):
    skill_query = request.GET.get('skill', '')
    location_query = request.GET.get('location', '')

    profiles = Hunarbaaz.objects.all()

    if skill_query:
        profiles = profiles.filter(skill__icontains=skill_query)

    if location_query:
        profiles = profiles.filter(location=location_query)

    skill_choices    = [c for c in Hunarbaaz.SKILL_CHOICES if c[0]]   # skip the empty placeholder
    location_choices = [c for c in Hunarbaaz.locations     if c[0]]

    context = {
        "profiles": profiles,               
        "skill_choices": skill_choices,     
        "location_choices": location_choices,
    }
    return render(request, "client/hunarbaaz_list.html", context)

@login_required
def hunarbaaz_detail_view(request, id):
    profile = get_object_or_404(Hunarbaaz, id=id)
    if hasattr(request.user, 'hunarbaaz'):
        raise Http404("Page not found") 
    return render(request, 'client/hunarbaaz_details.html', {'profile': profile})

@login_required
def create_work_request(request):
    hunarbaaz_id = request.GET.get('hunarbaaz_id')

    if request.method == 'POST':
        form = PostRequestForm(request.POST)
        if form.is_valid():
            work_request = form.save(commit=False)
            work_request.client = request.user
            work_request.save()
            return redirect('client:client_dashboard')  
    else:
        if hunarbaaz_id:
            form = PostRequestForm(initial={'hunarbaaz': hunarbaaz_id})
        else:
            form = PostRequestForm()

    return render(request, 'client/post_request.html', {'form': form})

@login_required
def request_history(request):
    requests = PostRequest.objects.filter(client=request.user).order_by('-created_at')
    return render(request, 'client/request_history.html', {'requests': requests})

@login_required
def request_status(request):
    status = request.GET.get('status', 'all')
    filter_by = status

    queryset = PostRequest.objects.filter(client=request.user)

    if status == 'pending':
        queryset = queryset.filter(is_accepted=None, is_cancelled=False)
    elif status == 'accepted':
        queryset = queryset.filter(is_accepted=True, is_cancelled=False)
    elif status == 'rejected':
        queryset = queryset.filter(is_accepted=False, is_cancelled=False)
    elif status == 'cancelled':
        queryset = queryset.filter(is_cancelled=True)

    return render(request, 'client/request_status.html', {
        'requests': queryset.order_by('-created_at'),
        'filter_by': filter_by
    })

@login_required
def cancel_request(request, request_id):
    post_request = get_object_or_404(PostRequest, id=request_id, client=request.user)

    if post_request.is_accepted is None:  # Only pending requests can be cancelled
        post_request.is_cancelled = True
        post_request.save()
    
    return redirect('client:request_status')

@login_required
def reschedule_request(request, pk):
    req = get_object_or_404(PostRequest, id=pk, client=request.user, is_accepted__isnull=True)
    if request.method == "POST":
        form = RescheduleRequestForm(request.POST, instance=req)
        if form.is_valid():
            form.save()
            messages.success(request, "Work request rescheduled.")
            return redirect("client:request_status")
    else:
        form = RescheduleRequestForm(instance=req)
    
    return render(request, "client/reschedule_request.html", {"form": form})

@login_required
def mark_as_completed(request, request_id):
    post_request = get_object_or_404(PostRequest, id=request_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=post_request)
        if form.is_valid():
            post_request.is_completed = True
            form.save()
            return redirect('client:request_history')
    else:
        form = ReviewForm(instance=post_request)

    return render(request, 'client/complete_review.html', {'form': form, 'post_request': post_request})