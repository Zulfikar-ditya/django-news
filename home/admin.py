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
        ('content', {'fields': (
                'content',
                ),
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
        'date_add',
        'name',
        'img',
        'new',
        'trending',
    ]
    search_fields = [
        'name',
    ]
    list_filter = [
        'new',
        'trending',
    ]
    ordering = ('new', 'trending', 'date_add')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)