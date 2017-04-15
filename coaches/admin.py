from django.contrib import admin
from coaches.models import Coach
# Register your models here.
class CoachAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'get_surname', 'gender', 'skype', 'description']
    list_filter = ['user__is_staff']


admin.site.register(Coach, CoachAdmin)