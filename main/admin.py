from django.contrib import admin
from main.models import Home, About, Services, Why_Us, Team


@admin.register(Home)
class Home(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)

@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('title', 'text_title',)
    list_display_links = ('title', 'text_title',)

@admin.register(Services)
class Services(admin.ModelAdmin):
    list_display = ('title', 'icon_title',)
    list_display_links = ('title', 'icon_title',)

@admin.register(Why_Us)
class Why_Us(admin.ModelAdmin):
    list_display = ('title', 'text',)
    list_display_links = ('title', 'text',)

@admin.register(Team)
class Team(admin.ModelAdmin):
    list_display = ('title', 'name', 'job',)
    list_display_links = ('title', 'name', 'job',)