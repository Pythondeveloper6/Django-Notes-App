from django.contrib import admin

# Register your models here.
from .models import Profile



class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user' , 'slug' , 'headline' , 'join_date']
    list_filter = ['headline' , 'join_date']
    search_fields = ['user__first_name' , 'headline' , 'bio']
    list_editable = ['headline']





admin.site.register(Profile , ProfileAdmin)
