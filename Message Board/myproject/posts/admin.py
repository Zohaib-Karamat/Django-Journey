from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['text_preview', 'created_at', 'admin_actions']
    list_filter = ['created_at']
    search_fields = ['text']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
    
    def text_preview(self, obj):
        """Show first 50 characters of the message"""
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Message Preview'
    
    def admin_actions(self, obj):
        """Show quick action links"""
        return 'Edit | Delete'
    admin_actions.short_description = 'Actions'

# Customize admin site headers
admin.site.site_header = 'Message Board Administration'
admin.site.site_title = 'Message Board Admin'
admin.site.index_title = 'Welcome to Message Board Admin Panel'
