from django.contrib import admin
from .models import User, UserConfirmation


# Register your models here.

class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'id', 'email', 'phone_number']


class UserConfirmationModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'verify_type']


admin.site.register(User, UserModelAdmin)
admin.site.register(UserConfirmation, UserConfirmationModelAdmin)

