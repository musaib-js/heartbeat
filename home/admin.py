from django.contrib import admin
from .models import donation_plea, donation

# Register your models here.
admin.site.register((donation_plea, donation))