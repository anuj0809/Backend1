from django.contrib import admin

from .models import User

# Register User model to show in admin panel
admin.site.register(User)