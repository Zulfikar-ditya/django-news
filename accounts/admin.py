from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserAdminCreationForm, UserAdminChangeForm

class MyUserAdmin(UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    list_display = [
        'username',
        'email',
        'full_name',
        'phone',
        'address',
        'avatar',
        'gender',
        'date_join',
        'date_of_birth',
        'is_superuser',
        'is_reporter',
        'is_staff',
        'is_active',
    ]
    search_fields = [
        'username',
        'full_name',
    ]
    list_filter = [
        'gender',
        'date_of_birth',
        'date_join',
        'is_superuser',
        'is_reporter',
        'is_staff',
        'is_active',
    ]
    fieldsets = (
        ('Personal Info', {'fields': (
            'full_name', 
            'email', 
            'phone',
            'avatar',
            'address',
            'date_of_birth',
                )
            }
        ),
        ('Username Password', {'fields': (
                'username',
                'password',
                )
            }
        ),
        ('Gender', {'fields': (
            'gender',
                )
            }
        ),
        ('Status', {'fields': (
                'is_superuser',
                'is_staff',
                'is_reporter',
                'is_active',
                )
            }
        )
    )
    filter_horizontal = ()
    ordering = ('id',)


admin.site.register(User, MyUserAdmin)
