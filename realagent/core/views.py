from django.shortcuts import render, redirect
from listing.models import Category, Location, Type, Listing
from .forms import SignupForm

# Create your views here.
def index(request):
    listings = Listing.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

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