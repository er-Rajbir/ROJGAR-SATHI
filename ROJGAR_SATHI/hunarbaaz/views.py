from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Hunarbaaz, WorkRequest
from .forms import HunarbaazProfileForm, HunarbaazUserForm
from django.http import HttpResponseForbidden
from django.db.models import Avg
from client.models import PostRequest

#for mail
from django.core.mail import send_mail
from django.conf import settings



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
            send_mail(
    'Welcome to Rozgaar Saathi!',
    f'Dear {profile.full_name},\n\nThank you for registering as a Hunarbaaz on Rozgaar Saathi!\n\nYour journey to new job opportunities starts now. \n Your Username is :{user.username}',
    settings.DEFAULT_FROM_EMAIL,
    [user.email],
    fail_silently=False,
)
            return redirect('login')
    else:
        user_form = HunarbaazUserForm()
        profile_form = HunarbaazProfileForm()

    return render(request, 'hunarbaaz/hunarbaaz_register.html', {
        'user_form': user_form,
        'profile_form': profile_form
})


@login_required
def hunarbaaz_dashboard(request):
    try:
        profile = Hunarbaaz.objects.get(user=request.user)
    except Hunarbaaz.DoesNotExist:
        return redirect('hunarbaaz:edit_profile')

    requests = PostRequest.objects.filter(hunarbaaz=profile)

    # Fetch recent reviews (only completed with non-null review and rating)
    recent_reviews = PostRequest.objects.filter(
        hunarbaaz=profile,
        is_completed=True,
        rating__isnull=False,
        review__isnull=False
    ).order_by('-created_at')[:4]

    # Calculate average rating
    average_rating = recent_reviews.aggregate(Avg('rating'))['rating__avg']
    average_rating = round(average_rating, 1) if average_rating else 0

    context = {
        'name': profile.full_name,
        'profile_pic': profile.profile_pic.url if profile.profile_pic else None,
        'location': profile.location,
        'skills': [profile.skill] if profile.skill else ['Not Set'],
        'aadhaar_verified': profile.is_verified,
        'pending_requests': requests.filter(is_accepted__isnull=True).count(),
        'ongoing_jobs': requests.filter(is_completed=False,is_accepted=True).count(),
        'completed_jobs': requests.filter(is_completed=True).count(),
        'rating': average_rating,
        'recent_reviews': recent_reviews
    }

    return render(request, 'hunarbaaz/dashboard.html', context)



@login_required
def edit_profile(request):
    try:
        hunarbaaz = Hunarbaaz.objects.get(user=request.user)
    except Hunarbaaz.DoesNotExist:
        return redirect('hunarbaaz:register_hunarbaaz')

    user = request.user

    if request.method == 'POST':
        user_form = HunarbaazUserForm(request.POST, instance=user)
        profile_form = HunarbaazProfileForm(request.POST, request.FILES, instance=hunarbaaz)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            # Handle password securely
        password = user_form.cleaned_data.get('password')
        if password:  # only if password was changed
            user.set_password(password)
            user.save()
        profile_form.save()
        return redirect('login')

    else:
        user_form = HunarbaazUserForm(instance=user)
        profile_form = HunarbaazProfileForm(instance=hunarbaaz)

    return render(request, 'hunarbaaz/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def view_requests(request):
    try:
        profile = Hunarbaaz.objects.get(user=request.user)
    except Hunarbaaz.DoesNotExist:
        return redirect('hunarbaaz:edit_profile')

    # ❌ Exclude cancelled requests
    requests = PostRequest.objects.filter(
        hunarbaaz=profile,
        is_cancelled=False  # This line excludes cancelled ones
    ).order_by('-created_at')

    return render(request, 'hunarbaaz/view_requests.html', {
        'client_requests': requests
    })

@login_required
def accept_request(request, request_id):
    req = get_object_or_404(PostRequest, id=request_id, hunarbaaz__user=request.user)
    req.is_accepted = True
    req.save()
      # Send email to the client
    client = req.client
    client_name = client.get_full_name() or client.username
    client_email = client.email

    hunarbaaz_name = req.hunarbaaz.full_name

    send_mail(
        subject='Your Job Request was Accepted ✅',
        message=f'Dear {client_name},\n\nGood news! Your job request has been accepted by {hunarbaaz_name}.\n\nThey will reach out to you shortly.\n\nRegards,\nRozgaar Saathi Team',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[client_email],
        fail_silently=False,
    )
    return redirect('hunarbaaz:view_requests')

@login_required
def reject_request(request, request_id):
    req = get_object_or_404(PostRequest, id=request_id, hunarbaaz__user=request.user)
    req.is_accepted = False
    req.save()
     # Send email to the client
    client = req.client
    client_name = client.get_full_name() or client.username
    client_email = client.email

    hunarbaaz_name = req.hunarbaaz.full_name

    send_mail(
        subject='Your Job Request was Rejected ❌',
        message=f'Dear {client_name},\n\nWe’re sorry! {hunarbaaz_name} has rejected your job request.\n\nYou can browse and connect with other Hunarbaaz on Rozgaar Saathi.\n\nRegards,\nRozgaar Saathi Team',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[client_email],
        fail_silently=False,)
    return redirect('hunarbaaz:view_requests')

@login_required
def mark_as_completed(request, request_id):
    post_request = get_object_or_404(PostRequest, id=request_id)

    # Only the assigned Hunarbaaz can mark the job as completed
    if post_request.hunarbaaz.user != request.user:
        return HttpResponseForbidden("You are not authorized to complete this request.")

    post_request.is_completed = True
    post_request.save()
    return redirect('hunarbaaz:view_requests')  # or 'hunarbaaz:work_history' if you prefer


@login_required
def work_history(request):
    profile = get_object_or_404(Hunarbaaz, user=request.user)
    
    completed_jobs = PostRequest.objects.filter(
        hunarbaaz=profile,
        is_completed=True
    ).order_by('-end_date', '-created_at')

    cancelled_jobs = PostRequest.objects.filter(
        hunarbaaz=profile,
        is_cancelled=True
    ).order_by('-end_date', '-created_at')

    return render(request, 'hunarbaaz/work_history.html', {
        'completed_jobs': completed_jobs,
        'cancelled_jobs': cancelled_jobs
    })

def public_work_history(request, hunarbaaz_id):
    profile = get_object_or_404(Hunarbaaz, id=hunarbaaz_id)

    completed_jobs = PostRequest.objects.filter(
        hunarbaaz=profile,
        is_completed=True
    ).order_by('-end_date', '-created_at')

    cancelled_jobs = PostRequest.objects.filter(
        hunarbaaz=profile,
        is_cancelled=True
    ).order_by('-end_date', '-created_at')

    return render(request, 'hunarbaaz/public_work_history.html', {
        'profile': profile,
        'completed_jobs': completed_jobs,
        'cancelled_jobs': cancelled_jobs
    })

@property
def full_name(self):
    return f"{self.user.first_name} {self.user.last_name}".strip()
