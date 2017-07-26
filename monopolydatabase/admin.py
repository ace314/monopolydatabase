from django.contrib import admin
from .models import*

class PlayersAdmin(admin.ModelAdmin):
    list_display = ["pk", "player_number", "bank_money", "pocket_money"]

class StockListAdmin(admin.ModelAdmin):
    list_display = ["pk", "stock_name", "stock_value"]

class PlayerStocksAdmin(admin.ModelAdmin):
    list_display = ["pk", "owned_player", "stock", "stock_amount"]

class LandAdmin(admin.ModelAdmin):
    list_display = ["land_name", "land_type", "owner", "houses"]



admin.site.register(player, PlayersAdmin)
admin.site.register(stock, StockListAdmin)
admin.site.register(players_stock_list, PlayerStocksAdmin)
admin.site.register(land, LandAdmin)

# Register your models here.
