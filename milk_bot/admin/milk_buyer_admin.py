from django.contrib import admin

from milk_bot.models import MilkBuyer


@admin.register(MilkBuyer)
class MilkBuyerAdmin(admin.ModelAdmin):
    list_display = ["full_name", "position"]
