from django.contrib import admin
from .models import UsersMessages


@admin.register(UsersMessages)
class UsersMessagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'message', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'message', 'email')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('id', 'created_at')
