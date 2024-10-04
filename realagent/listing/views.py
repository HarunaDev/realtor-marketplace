from django.shortcuts import render, get_object_or_404
from .models import Listing
# Create your views here.

# create view for apartment detail
def detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    related_items = Listing.objects.filter(location=listing.location, is_sold=False).exclude(pk=pk)[:3]

    return render(request, 'listing/detail.html', {
        'listing': listing,
        'related_items': related_items
    })
