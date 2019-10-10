from django.contrib import admin
from .models import Location,Photos,Category
# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    filter_horizontal =('loca',)

admin.site.register(Location)
admin.site.register(Photos,GalleryAdmin)
admin.site.register(Category)
