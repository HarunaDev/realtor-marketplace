from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from .forms import NewListingForm, EditListingForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# create view for apartment detail
def detail(request, pk):
    account_type = None
    if request.user.is_authenticated:
        account_type = request.user.userprofile.profile_type
    listing = get_object_or_404(Listing, pk=pk)
    properties = Listing.objects.filter(is_sold=False).exclude(pk=pk)[0:6]
    related_items = Listing.objects.filter(location=listing.location, is_sold=False).exclude(pk=pk)[:3]

    return render(request, 'listing/detail.html', {
        'listing': listing,
        'related_items': related_items,
        'properties': properties,
        'account_type': account_type      
    })

@login_required
def new(request):
    account_type = request.user.userprofile.profile_type
    if request.method == 'POST':
        form = NewListingForm(request.POST, request.FILES)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.created_by = request.user
            listing.save()

            return redirect('listing:detail', pk=listing.id)
    else:
        form = NewListingForm()

    return render(request, 'listing/form.html', {
        'form': form,
        'title': 'New Listing Form',
        'account_type': account_type,
    })

@login_required
def edit(request, pk):
    account_type = request.user.userprofile.profile_type
    listing = get_object_or_404(Listing, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditListingForm(request.POST, request.FILES, instance=listing)

        if form.is_valid():
            form.save()

            return redirect('listing:detail', pk=listing.id)
    else:
        form = EditListingForm(instance=listing)
    
    return render(request, 'listing/form.html', {
        'form': form,
        'title': 'Edit Item',
        'account_type': account_type,
    })

@login_required
def delete(request, pk):
    listing = get_object_or_404(Listing, pk=pk, created_by=request.user)
    listing.delete()

    return redirect('core:index')