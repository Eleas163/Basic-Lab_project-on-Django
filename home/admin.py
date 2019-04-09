from django.contrib import admin
from .models import Photo
# Register your models here.
class Photo_Admin(admin.ModelAdmin):
	list_display = ['title', 'upload_time']

    class Meta:
    	model = Photo
admin.site.Register(Photo, Photo_Admin)    	
	
