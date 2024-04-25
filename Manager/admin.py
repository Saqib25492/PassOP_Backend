from django.contrib import admin
from Manager.models import User, Passwords
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email"]
    
    
class PasswordsAdmin(admin.ModelAdmin):
    list_display = ['site', "username", "password"]


admin.site.register(User, UserAdmin)
admin.site.register(Passwords, PasswordsAdmin)
