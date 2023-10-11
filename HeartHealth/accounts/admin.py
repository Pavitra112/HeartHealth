from django.contrib import admin
from accounts.models import UserProfileInfo
# Register your models here.
class UserProfile(admin.ModelAdmin):
    list_display = ('user', 'profile_pic')
admin.site.register(UserProfileInfo,UserProfile)

