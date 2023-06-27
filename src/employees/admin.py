from django.contrib import admin

from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Add employee to admin."""
    list_display = ('username', 'email', 'is_active', 'is_staff',)
