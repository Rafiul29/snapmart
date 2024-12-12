from django.contrib import admin
from .models import UserAccount
# Register your models here.

class UserAdmin(admin.ModelAdmin):
  list_display=['id','username','first_name','last_name','email','role']

admin.site.register(UserAccount,UserAdmin)

