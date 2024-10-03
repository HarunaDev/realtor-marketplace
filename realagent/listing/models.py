from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Category model
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
# Location model
class Location(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name

# Type model
class Type(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Types"

    def __str__(self):
        return self.name

# Listing model
class Listing(models.Model):
    category = models.ForeignKey(Category, related_name='apartments', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='apartments', on_delete=models.CASCADE)
    type = models.ForeignKey(Type, related_name='apartments', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='apartments', on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='listing_media', blank=True, null=True)
    large = models.ImageField(upload_to='listing_media', blank=True, null=True)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = "Listings"

    def __str__(self):
        return self.title