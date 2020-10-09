from django.contrib import admin

from .models import Category, Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'date_add',
        'image',
        'reporter',
        'categorie',
        'status',
        'viewer',
    ]
    list_filter = [
        'status',
        'reporter',
        'date_add',
        'categorie',
    ]
    search_fields = [
        'title',
        'reporter',
    ]
    fieldsets = (
        ('None', {'fields': (
            'title',
            'image',
            'reporter',
            'categorie',
                )
            }
        ),
        ('status', {'fields': (
            'status',
                )
            }
        ),
        ('view', {'fields': (
            'viewer',
                )
            }
        )
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'img',
    ]
    search_fields = [
        'name'
    ]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)