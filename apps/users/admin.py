from django.contrib import admin

from apps.users.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # list_filter = ('username', )
    list_display = ('id','username', 'email', 'date_joined', 'phone')
    search_fields = ('username', 'email', 'date_joined', 'phone')
admin.site.register(User, UserAdmin)