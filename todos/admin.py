from django.contrib import admin
from .models import Task


class TaskDisplay(admin.ModelAdmin):
    list_display = ('task', 'is_completed',)
    
    
admin.site.register(Task, TaskDisplay)