from django.contrib import admin
from .models import *
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter
# from related_admin import RelatedFieldAdmin

class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'science', 'userball', 'maxball']
    list_display_links = ['id', 'user']
    list_filter = [('science', RelatedDropdownFilter)]
admin.site.register(Result, ResultAdmin)

