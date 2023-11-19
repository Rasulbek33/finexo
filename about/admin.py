from django.contrib import admin
from about.models import About

@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('title', 'text_title')
    list_display_links = ('title',  'text_title')