from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'user_type', 'first_name', 'last_name', 'address', 'phone']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Information', {'fields': ('user_type', 'first_name', 'last_name', 'address', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_type', 'first_name', 'last_name', 'address', 'phone', 'email', 'password1', 'password2'),
        }),
    )
    ordering = ['email']


admin.site.register(CustomUser, CustomUserAdmin)
