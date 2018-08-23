from django.contrib import admin

# Register your models here.

from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'email', 'c_time',)

admin.site.register(User, UserAdmin)


class ConfirmStringAdmin(admin.ModelAdmin):
    list_display = ('user', 'c_time', 'code')

admin.site.register(ConfirmString, ConfirmStringAdmin)