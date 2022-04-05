from django.contrib import admin
from related_admin import RelatedFieldAdmin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter
from .models import *

class Science_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'author')
    list_display_links = ('id', 'name', 'author')
    list_filter = [('name', DropdownFilter)]

admin.site.register(Science, Science_Admin)

class Question_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'science')
    list_display_links = ('id', 'name')
    list_filter = [('science', RelatedDropdownFilter)]

admin.site.register(Question, Question_Admin)

