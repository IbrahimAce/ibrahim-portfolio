from django.contrib import admin
from .models import Project, Experience, Education, ContactMessage, Skill


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'featured', 'created')
    list_editable = ('featured',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'period', 'order')
    list_editable = ('order',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('qualification', 'institution', 'period', 'order')
    list_editable = ('order',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created', 'read')
    list_editable = ('read',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'created')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'category')
