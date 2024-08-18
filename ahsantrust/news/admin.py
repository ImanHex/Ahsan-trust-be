from django.contrib import admin
from .models import news
from .forms import NewsAdminForm


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ("name", "Date")
    list_display_links = ("name",)
    form = NewsAdminForm


admin.site.register(news, NewsAdmin)
