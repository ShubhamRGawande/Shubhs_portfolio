from django.contrib import admin
from .models import Contact  # Import the Contact model

# Register the Contact model
admin.site.register(Contact)
admin.site.site_header = "My Portfolio Admin Panel"
admin.site.site_title = "Admin | Portfolio"
admin.site.index_title = "Welcome to My Portfolio Admin"
