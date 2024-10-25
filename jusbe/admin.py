from django.contrib import admin
from .models import CustomUser, Category, Remind

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    search_fields = ('email',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


class RemindAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'memo' , 'due_datetime', 'is_checked', 'user')


admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Remind, RemindAdmin)
