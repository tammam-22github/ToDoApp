from django.contrib import admin
from .models import Tasks
# Register your models here.

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display=['title','complete','created']
    list_filter=['title','complete']
    search_fields=['title','complete']
    date_hierarchy='created'