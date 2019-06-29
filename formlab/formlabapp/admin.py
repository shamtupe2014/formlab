from django.contrib import admin
from .models import userinfo,registration

class userinfoAdmin(admin.ModelAdmin):
    list_display =["First_name","Last_name","Email_ID","Mobile_No","Date_Of_Birth","Photo","Remark"]

class registrationAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "birthday", "city", "email", "phone"]


admin.site.register(userinfo,userinfoAdmin)
admin.site.register(registration,registrationAdmin)

