from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import User,activity_periods


class UserAdmin(ModelAdmin):
   list_display = ['id','real_name','tz']
   
class ActivityAdmin(ModelAdmin):
    list_dsipaly = ['activity_id','start_time','end_time']
   
   
admin.site.register(activity_periods,ActivityAdmin)
admin.site.register(User,UserAdmin)
