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


class VideoInline(admin.TabularInline):
    model = Video


class SubjectAdmin(admin.ModelAdmin):
    inlines = [VideoInline,]


admin.site.register(Level)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Video, VideoAdmin)