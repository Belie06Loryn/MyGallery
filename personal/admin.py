from django.contrib import admin
from .models import Location,Photos,Category

class GalleryAdmin(admin.ModelAdmin):
    admin.site.register(Location)
    admin.site.register(Photos)
    admin.site.register(Category)
