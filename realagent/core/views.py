from django.shortcuts import render, redirect
from listing.models import Category, Location, Type, Listing, UserProfile
from .forms import SignupForm
from django.contrib.auth import logout

def index(request):
    listings = Listing.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    # Accessing the username and account type if authenticated
    if request.user.is_authenticated:
        username = request.user.username
        account_type = request.user.userprofile.profile_type
    else:
        username = "Guest"
        account_type = None

    return render(request, "core/index.html", {
        'categories': categories,
        'listings': listings,
        'username': username,
        'account_type': account_type
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout_view(request):
    logout(request)
    return redirect('core:index')
