from django.contrib import admin
from .models import*

class PlayersAdmin(admin.ModelAdmin):
    list_display = ["pk", "player_number", "bank_money", "pocket_money", "poisoned"]

class StockListAdmin(admin.ModelAdmin):
    list_display = ["pk", "stock_name", "stock_value"]

class PlayerStocksAdmin(admin.ModelAdmin):
    list_display = ["pk", "owned_player", "stock", "stock_amount"]

class LandAdmin(admin.ModelAdmin):
    list_display = ["pk", "land_name", "land_type", "land_value", "owner", "houses"]

class StockRandomList(admin.ModelAdmin):
    list_display = ["pk", "stockname","risefall", "index"]

class MansionList(admin.ModelAdmin):
    list_display = ["tag", "name", "money"]


admin.site.register(player, PlayersAdmin)
admin.site.register(stock, StockListAdmin)
admin.site.register(players_stock_list, PlayerStocksAdmin)
admin.site.register(land, LandAdmin)
admin.site.register(stock_random_risefall_list, StockRandomList)
admin.site.register(mansion, MansionList)

# Register your models here.
