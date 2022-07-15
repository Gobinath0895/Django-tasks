from django.contrib import admin
from crud_app.models import Student

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list = ['sno', 'sname', 'sclass', 'saddress']
admin.site.register(Student, studentAdmin)
