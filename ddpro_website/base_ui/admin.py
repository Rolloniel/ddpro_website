from django.contrib import admin
from .models import About, TeamMember, Product


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
   list_display = ['heading', 'text_html']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
   list_display = ['first_name', 'last_name', 'image', 'priority', 'roles']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ['title', 'image', 'short_description']