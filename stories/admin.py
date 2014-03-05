from django.contrib import admin
from stories.models import Story

# Register your models here.

class StoryAdmin(admin.ModelAdmin):
    list_display=('__unicode__', 'url', 'moderator', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'moderator__username', 'moderator__first_name'
            ,'moderator__last_name')
    # def lower_case_title(self, obj):
        # return obj.title.lower()
    # lower_case_title.short_description = 'title'

admin.site.register(Story, StoryAdmin)
