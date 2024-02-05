from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from account.models import User, Otp


class UserAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('phone', 'email', 'avatar', 'is_active', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('اطلاعات شخصی', {'fields': ('fullname', 'phone')}),
        (' تصویر', {'fields': ('avatar',)}),
        ('دسترسی ها', {'fields': ('is_admin', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
         (None, {'fields': ('email', 'password')}),
        ('اطلاعات شخصی', {'fields': ('fullname', 'phone')}),
        (' تصویر', {'fields': ('avatar',)}),
        ('دسترسی ها', {'fields': ('is_admin', 'is_active')}),

    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# admin.site.register(Address)
# Now register the new UserAdmin...


admin.site.register(User, UserAdmin)
admin.site.register(Otp)

# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
