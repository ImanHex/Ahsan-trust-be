from django.contrib import admin
from .form import AnnounceAdminForm
from .models import announce

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ["title"]
    form = AnnounceAdminForm

admin.site.register(announce, AnnouncementAdmin)
