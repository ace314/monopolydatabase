from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class stock(models.Model):
    stock_name = models.CharField(max_length=100, blank=True)
    stock_value = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.stock_name

class player(models.Model):
    player_number = models.PositiveIntegerField(default=0)
    bank_money = models.PositiveIntegerField(default=0)
    pocket_money = models.PositiveIntegerField(default=0)
    poisoned = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.player_number)

class players_stock_list(models.Model):
    owned_player = models.ForeignKey(player, on_delete=models.CASCADE)
    stock = models.ForeignKey(stock, on_delete = models.CASCADE)
    stock_amount = models.PositiveIntegerField(default=0)

class land(models.Model):
    land_name = models.CharField(max_length=100, blank=True)
    land_type = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(3)])
    owner = models.ForeignKey(player, on_delete=models.CASCADE)
    houses = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(999999)])


# Create your models here.
