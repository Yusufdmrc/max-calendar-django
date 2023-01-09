from django.contrib import admin
from .models import Scheduling

class SchedulingAdmin(admin.ModelAdmin):
    list_display=('id','name','location','created_date')
    list_display_links=('id','name')
    list_filter=('created_date',)
    search_fields=('name','description')
    list_per_page=20

# Register your models here.

admin.site.register(Scheduling)