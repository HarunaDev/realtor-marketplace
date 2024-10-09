from django.contrib import admin
from .models import Category, Location, Type, Listing, UserProfile

# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Type)
admin.site.register(Listing)
admin.site.register(UserProfile)  # Register UserProfile to admin
