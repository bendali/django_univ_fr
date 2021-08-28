from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
   list_display = ('name', 'description', 'due_date',
                   'schedule_date', 'closed', )
   read_only= ('created_date')
admin.site.register(Task,TaskAdmin)