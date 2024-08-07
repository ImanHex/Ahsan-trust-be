from django.contrib import admin
from .models import stores
from .forms import StoresAdminForm
 


# Register your models here.
class StoresAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "categories", "phone", "time")
    list_display_links = ("name",)
    form = StoresAdminForm


admin.site.register(stores, StoresAdmin)
