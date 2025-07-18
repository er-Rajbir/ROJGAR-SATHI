from django.contrib import admin
from .models import ClientProfile,PostRequest

class client(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'phone', 'created_at')
    list_filter = ('gender', 'created_at')
    search_fields = ('full_name', 'phone', 'user__username', 'address')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('User Association', {
            'fields': ('user',)
        }),
        ('Personal Details', {
            'fields': ('full_name', 'gender', 'phone', 'address', 'profile_picture')
        }),
        ('Account Creation Info', {
            'fields': ('created_at',)
        }),
    )

admin.site.register(ClientProfile,client)

class postrequest(admin.ModelAdmin):
    list_display = ('client', 'hunarbaaz', 'job_type', 'location', 'start_date', 'end_date')
    list_filter = ('job_type', 'is_accepted', 'is_completed', 'is_cancelled', 'start_date', 'end_date')
    search_fields = ('client__username', 'hunarbaaz__full_name', 'location', 'job_description')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Client and Hunarbaaz', {
            'fields': ('client', 'hunarbaaz')
        }),
        ('Job Details', {
            'fields': ('job_description', 'location', 'job_type', 'working_hours', 'start_date', 'end_date')
        }),
        ('Request Status', {
            'fields': ('is_accepted', 'is_completed', 'is_cancelled')
        }),
        ('Review & Rating', {
            'fields': ('rating', 'review')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )

admin.site.register(PostRequest, postrequest)



