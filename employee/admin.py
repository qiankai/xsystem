from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from models import *


class AccountInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'


class UserAdmin(BaseUserAdmin):
    inlines = (AccountInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
