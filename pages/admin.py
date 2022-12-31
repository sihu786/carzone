from django.contrib import admin

from pages.models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def Photo(self,object):
        return format_html('<img src="{}" width="40"/>'.format(object.photo.url))
    
    list_display=('id','first_name','Photo','designation','create_date')
    list_display_links=('first_name','id','Photo')
    search_fields=('id','first_name','last_name','designation')
admin.site.register(Team,TeamAdmin)