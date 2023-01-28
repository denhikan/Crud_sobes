from django.contrib import admin
from .models import *


class SelectDepAdmin(admin.ModelAdmin):
    list_display = ["name_department"]

class StaffAdmin(admin.ModelAdmin):
    list_display = ["name", "department", "register_date"]

admin.site.register(SelectDep, SelectDepAdmin)
admin.site.register(Staff, StaffAdmin)