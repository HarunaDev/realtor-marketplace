from django.shortcuts import render, redirect
from listing.models import Category, Location, Type, Listing
from .forms import SignupForm
from django.contrib.auth import logout

# Create your views here.
def index(request):
    listings = Listing.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    # Accessing the username
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Guest"

    return render(request, "core/index.html", {
        'categories': categories,
        'listings': listings 
    })

def signup(request):
    # validate form before creating user
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

# def login(request):
#     return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('core:index')