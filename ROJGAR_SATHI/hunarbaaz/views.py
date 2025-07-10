from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Hunarbaaz, WorkRequest
from .forms import HunarbaazProfileForm, HunarbaazUserForm
from django.http import HttpResponseForbidden


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
            return redirect('login')
    else:
        user_form = HunarbaazUserForm()
        profile_form = HunarbaazProfileForm()

    return render(request, 'hunarbaaz/hunarbaaz_register.html', {
        'user_form': user_form,
        'profile_form': profile_form
})

from client.models import PostRequest

@login_required
def hunarbaaz_dashboard(request):
    try:
        profile = Hunarbaaz.objects.get(user=request.user)
    except Hunarbaaz.DoesNotExist:
        return redirect('hunarbaaz:edit_profile')

    # Fetch requests related to this hunarbaaz
    requests = PostRequest.objects.filter(hunarbaaz=profile)

    # Calculate status counts
    ongoing_jobs = requests.filter(is_completed=False).count()
    completed_jobs = requests.filter(is_completed=True).count()
    pending_requests = PostRequest.objects.filter(hunarbaaz=profile, is_accepted__isnull=True).count() # If you add a completion field, update this
    rating = 4.7  # Placeholder, if you implement rating system

    context = {
        'name': profile.full_name,
        'profile_pic': profile.profile_pic.url if profile.profile_pic else None,
        'location': profile.location,
        'skills': [profile.skill] if profile.skill else ['Not Set'],
        'aadhaar_verified': profile.is_verified,
        'pending_requests': pending_requests,
        'ongoing_jobs': ongoing_jobs,
        'completed_jobs': completed_jobs,
        'rating': rating,
        'recent_reviews': []  # Later you can link reviews here
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
            profile_form.save()
            return redirect('hunarbaaz:hunarbaaz_dashboard')

    else:
        user_form = HunarbaazUserForm(instance=user)
        profile_form = HunarbaazProfileForm(instance=hunarbaaz)

    return render(request, 'hunarbaaz/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })




# list of hunrabaaaz



#dashboard requests
from client.models import PostRequest

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
    return redirect('hunarbaaz:view_requests')

@login_required
def reject_request(request, request_id):
    req = get_object_or_404(PostRequest, id=request_id, hunarbaaz__user=request.user)
    req.is_accepted = False
    req.save()
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