from django.contrib import admin
from .models import Hunarbaaz
# Register your models here.
class hunarbaaz(admin.ModelAdmin):
    list_display = ('full_name','gender','skill','location','is_verified')
    list_filter = ['gender','skill','location','is_verified']
    readonly_fields = ['created_at']
    search_fields = ['full_name','skill','location']
    fieldsets = (
        ('User Association', {
            'fields': ('user',)
        }),
        ('Personal Information', {
            'fields': ('full_name', 'mobile', 'gender','aadhaar_number','profile_pic')
        }),
        ('Skill Details', {
            'fields': ('skill', 'experience', 'location','wages','is_verified')
        }),
        ('Work Sample', {
            'fields': ('work_sample_1', 'work_sample_2', 'work_sample_3')
        }),
        ('Account Creation',{
            'fields': ('created_at',)
        }),
    )
admin.site.register(Hunarbaaz,hunarbaaz)

admin.site.site_header = "Rozgaar Saathi Admin Dashboard"
admin.site.site_title = "Rozgaar Saathi Admin Portal"