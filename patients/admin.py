from django.contrib import admin

from patients.models import Appointment, Contact, Department, Doctor

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Contact)

#update or deactivate entries instead of deleting them
#admin customization to toggle the is_active status of departments,doctors and services without deleting them
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)    #Allows quick updates of the is_active field directly from the admin list view

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','department','is_active')
    list_editable = ('is_active',)



