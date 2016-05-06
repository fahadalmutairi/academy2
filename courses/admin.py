from django.contrib import admin

# Register your models here.
from courses.models import Subject, Level, Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'video_order', 'video_id', 'available']
    list_filter = ['date_published']
    search_fields = ['title']
    list_editable = ['title', 'video_id', 'available']
    list_display_links = ['subject']
    class Meta:
        model = Video


admin.site.register(Level)
admin.site.register(Subject)
admin.site.register(Video, VideoAdmin)