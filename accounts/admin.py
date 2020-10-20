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
    ordering = ('id',)
    filter_horizontal = ()

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj)
        is_superuser = request.user.is_superuser
        disable_fields = set()
        if not is_superuser:
            disable_fields |= {
                'username',
                'email',
                'full_name',
                'phone',
                'address',
                'avatar',
                'gender',
                'date_of_birth',
                'is_superuser',
                'is_reporter',
                'is_active',
                'is_staff',
            }
            if (
                not is_superuser
                and obj is not None
                and obj == request.user
            ):
                disable_fields |= {
                'username',
                'email',
                'full_name',
                'phone',
                'address',
                'avatar',
                'gender',
                'date_of_birth',
                'is_superuser',
                'is_reporter',
                'is_active',
                'is_staff',
                }
        for i in disable_fields:
            if i in form.base_fields:
                form.base_fields[i].disabled = True
        return form


admin.site.register(User, MyUserAdmin)
