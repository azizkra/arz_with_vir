from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import NewUser, Profile
# Register your models here.

admin.site.register(Profile)

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
    ordering=('email',)
    
    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('email', 'username', 'password1', 'password2' , 'is_admin', 'is_staff'),
        }),
    )
    

admin.site.register(NewUser, AccountAdmin)