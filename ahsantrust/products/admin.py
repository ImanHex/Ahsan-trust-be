from django.contrib import admin
from .models import Product, ProductImage
from .forms import ProductAdminForm, ProductImageForm


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    form = ProductImageForm
    extra = 1
    readonly_fields = ("image_url",)




# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ("store", "name", "categories")
    list_display_links = ("name",)
    inlines = [ProductImageInline]



admin.site.register(Product, ProductAdmin)
