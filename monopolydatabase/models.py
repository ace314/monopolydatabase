from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator

class stock(models.Model):
    stock_name = models.CharField(max_length=100, blank=True)
    stock_value = models.IntegerField(default=0)
#    last_ups_and_downs = models.PositiveIntegerField(default=0)     #上次漲跌幅
#    is_controlled = models.PositiveIntegerField(default=0)          #0=沒被控制 1=被控制
#    controlled_ups_and_downs = models.PositiveIntegerField(default=0)       #下次直接輸入的漲幅
    def __str__(self):
        return self.stock_name

class player(models.Model):
    player_number = models.IntegerField(default=0)
    bank_money = models.IntegerField(default=0)
    pocket_money = models.IntegerField(default=0)
    poisoned = models.IntegerField(default=0)

    def __str__(self):
        return str(self.player_number)

class players_stock_list(models.Model):
    owned_player = models.ForeignKey(player, on_delete=models.CASCADE)
    stock = models.ForeignKey(stock, on_delete = models.CASCADE)
    stock_amount = models.IntegerField(default=0)

class land(models.Model):
    land_name = models.CharField(max_length=100, blank=True)
    land_type = models.IntegerField(default=0, validators=[MaxValueValidator(3)])
    land_value = models.IntegerField(default=0)
    owner = models.ForeignKey(player, on_delete=models.CASCADE)
    houses = models.IntegerField(default=0, validators=[MaxValueValidator(999999)])

    def __str__(self):
        return str(self.land_name)

class stock_random_risefall_list(models.Model):
    stockname = models.ForeignKey(stock, on_delete=models.CASCADE)
    risefall = models.IntegerField(default=0)
    index = models.IntegerField(default=0)


# Create your models here.
