from django.contrib import admin
from .models import Teams
# Register your models here.
class TeamAdmin(admin.ModelAdmin):

    list_display=('id','first_name','last_name','designation','created_date')
    list_display_links=('id','first_name','designation')
    search_fields=('first_name','designation')
    list_filter=('designation',)
admin.site.register(Teams,TeamAdmin)
