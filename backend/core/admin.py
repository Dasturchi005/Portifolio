# admin.py
from django.contrib import admin
from .models import Project, Skill, ContactRequest

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'order', 'created_at')
    list_filter = ('is_featured', 'technologies')
    search_fields = ('title', 'description')
    list_editable = ('is_featured', 'order')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'category', 'order')
    list_editable = ('percentage', 'order')

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read',)
    search_fields = ('name', 'email', 'subject')