from django.contrib import admin
from .models import Category, Inventory, UserWallet


admin.site.register(Category)
admin.site.register(UserWallet)
# Register your models here.


@admin.register(Inventory)
class ShosekiLinksAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity']
