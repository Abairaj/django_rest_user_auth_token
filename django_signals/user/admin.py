from django.contrib import admin
from.models import users

# Register your models here.

class usersAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','mobile','date_joined')


admin.site.register(users,usersAdmin)