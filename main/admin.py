from django.contrib import admin
from main.models import *

# Register your models here.

class Todo(admin.ModelAdmin):
    list_display = ('title', 'description', 'sent_at')


admin.site.register(ToDo)