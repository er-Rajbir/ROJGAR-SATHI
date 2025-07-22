from django.contrib import admin
from .models import ContactReview

class ContactReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user_type', 'query_type', 'submitted_at')
    list_filter = ('user_type', 'query_type', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('submitted_at',)

    fieldsets = (
        ('User Info', {
            'fields': ('name', 'email', 'user_type')
        }),
        ('Query Details', {
            'fields': ('query_type', 'message')
        }),
        ('Meta', {
            'fields': ('submitted_at',)
        }),
    )
admin.site.register(ContactReview,ContactReviewAdmin)