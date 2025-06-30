from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  PersonProfile, Attendance,QRData



# PersonProfile ကို Register
@admin.register(PersonProfile)
class PersonProfileAdmin(admin.ModelAdmin):
    list_display = ('user','name',) # မိမိ model field အရ ပြင်နိုင်တယ်

# Attendance ကို Register
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('person', 'timestamp', 'action','date')
    # list_filter = ('date',)
    search_fields = ('person__user__username',)
admin.site.register(QRData)