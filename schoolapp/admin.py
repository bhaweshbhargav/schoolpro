from django.contrib import admin
from .models import School


# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name','university_name')


admin.site.register(School, SchoolAdmin)
