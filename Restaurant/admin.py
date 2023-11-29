from django.contrib import admin
from .models import Booking, Menu

# Register your models here.
admin.site.site_header = "LittleLemon Restaurant"
admin.site.site_title = "LittleLemon Restaurant Admin Portal"
admin.site.index_title = "Welcome to LittleLemon Restaurant Portal"

admin.site.register(Booking)
admin.site.register(Menu)
