from django.shortcuts import render
from rest_framework.views import APIView
from random import randint
from django.db.models import Q
from django.http import HttpResponse

from .models import player, stock, players_stock_list, land, stock_random_risefall_list
# Create your views here.

#TODO:從random_list中取值改變股票價值; 各種更新時的calling
class Addmoney_bank(APIView):

    def get(self, request, recieverpk, money):
        reciever = player.objects.get(pk=recieverpk)
        mon = int(money)
        if mon<0:
            if (reciever.bank_money<abs(mon)):
                not_enough_money_response = u'存款餘額不足，將被歸零!\n'
                return HttpResponse(not_enough_money_response)
            else:
                reciever.bank_money += mon
                reciever.save()
                success_response = u'銀行成功扣款!\n'
                return HttpResponse(success_response)
        else:
            reciever.bank_money += mon
        reciever.save()
        success_response = u'銀行成功入帳!\n'
        return HttpResponse(success_response)

class Addmoney_pocket(APIView):

    def get(self, request, recieverpk, money):
        reciever = player.objects.get(pk=recieverpk)
        mon = int(money)
        if mon<0:
            if (reciever.pocket_money<abs(mon)):
                not_enough_money_response = u'現金餘額不足，將被歸零!\n'
                return HttpResponse(not_enough_money_response)
            else:
                reciever.pocket_money += mon
                reciever.save()
                success_response = u'成功支付現金!\n'
                return HttpResponse(success_response)
        else:
            reciever.pocket_money += mon
        reciever.pocket_money += mon
        reciever.save()
        success_response = u'成功獲得現金!\n'
        return HttpResponse(success_response)

class Got_knife(APIView):   #獲得刀傷

    def get(self, request, recieverpk):
        reciever = player.objects.get(pk=recieverpk)
        reciever.poisoned += 1
        reciever.save()
        success_give_knife_response = u'成功給予刀傷!'
        return HttpResponse(success_give_knife_response)

class Cure_knife(APIView):  #醫院治療刀傷

    def get(self, request, recieverpk):
        reciever = player.objects.get(pk=recieverpk)
        reciever.poisoned = 0
        reciever.save()
        playernumber = str(reciever.player_number)
        success_cure_response = u'成功治療第' + playernumber + u'小隊的所有刀傷!'
        return HttpResponse(success_cure_response)

class Got_land(APIView):

    def get(self, request, playerpk, landpk, get_or_loss):     #get_or_loss: get=1  ;   loss=0
        if (land.objects.filter(pk=landpk).exists()):
            landing = land.objects.get(pk=landpk)
            if (int(get_or_loss)==1):   #get or loss
                if (int(landing.owner.player_number)==0):    #無主地
                    reciever = player.objects.get(pk=playerpk)
                    landvalue = landing.land_value
                    if (reciever.pocket_money < landvalue):     #錢不夠買地
                        not_enough_money_response = u'現金餘額不足!\n'
                        return HttpResponse(not_enough_money_response)
                    else:                                       #錢夠買地，購買成功
                        landing.owner = reciever
                        landing.save()
                        success_get_response = u'土地' + u'購買成功!\n'
                        return HttpResponse(success_get_response)
                else:
                    error_get_response = u'買別人土地甚麼心態，購買失敗!\n'
                    return HttpResponse(error_get_response)

            else:
                x = player.objects.get(pk=11)
                landing.owner = x
                landing.houses = 0
                landing.save()
                a = str(landing.land_name)
                success_loss_response = u'土地' + a + u'已成為無主地!\n'
                return HttpResponse(success_loss_response)
        else:
            error_landnonexist_response = u'土地不存在!\n'
            return HttpResponse(error_landnonexist_response)

class Get_house(APIView):
    def get(self, request, playerpk, landpk, amount):
        landing = land.objects.get(pk=landpk)
        if (landing.owner.player_number == int(playerpk)):  #土地確實為買房者擁有
            amo = int(amount)
            a = str(landing.land_name)
            b = str(abs(amo))
            if (amo >= 1):
                landing.houses += amo
                landing.save()
                success_response = u'成功為' + a + u'增加' + b + u'棟房子'
                return HttpResponse(success_response)
            else:
                if(landing.houses < abs(amo)):
                    not_enough_houses_response = u'房子不夠拆啦，拆少點或別拆好嗎TAT\n'
                    return HttpResponse(not_enough_houses_response)
                else:
                    landing.houses += amo
                    landing.save()
                    success_response = u'成功為' + a + u'減少' + b + u'棟房子'
                    return HttpResponse(success_response)
        else:
            not_true_owner_response = u'請不要秀財產幫別人的地蓋房好嗎!\n'
            return HttpResponse(not_true_owner_response)

class stockss(APIView):

    def get(self, request, playerpk, stockpk, amount):
        if(stock.objects.filter(pk=stockpk).exists()):
            stocking = stock.objects.get(pk=stockpk)
            value = stocking.stock_value
            buyer = player.objects.get(pk=playerpk)
            stock_list = self.get_correct_player_stock_list(playerpk)    #某玩家持有所有股票列表
            target_stock_record = stock_list.get(stock=stocking)    #從上一行列表找出目標股票持有資料
            amo = int(amount)
            cost = value*amo
            if(amo >= 0):
                if (buyer.bank_money < cost):
                    not_enough_money_response = u'銀行餘額不足!\n'
                    return HttpResponse(not_enough_money_response)
                else:
                    buyer.bank_money -= cost
                    target_stock_record.stock_amount += amo
                    buyer.save()
                    target_stock_record.save()
                    stock_name = str(stocking.stock_name)
                    amount_unicode = str(amo)
                    success_buy_response = u'成功購買股票' + stock_name + u'，共計' + amount_unicode + u'股!\n'
                    return HttpResponse(success_buy_response)
            else:
                if (target_stock_record.stock_amount < abs(amo)):
                    not_enough_stock_response = u'持有股票不足!\n'
                    return HttpResponse(not_enough_stock_response)
                else:
                    buyer.bank_money -= cost
                    target_stock_record.stock_amount += amo
                    buyer.save()
                    target_stock_record.save()
                    stock_name = str(stocking.stock_name)
                    amount_unicode = str(abs(amo))
                    success_sell_response = u'成功販賣股票' + stock_name + u'，共計' + amount_unicode + u'股!\n'
                    return HttpResponse(success_sell_response)
        else:
            stock_nonexist_response = u'股票不存在!\n'
            return HttpResponse(stock_nonexist_response)


    def get_correct_player_stock_list(self, playerpk):
        user = player.objects.get(pk=playerpk)
        user_stock_list = players_stock_list.objects.filter(owned_player=user)
        return user_stock_list

class change_stock_risefall(APIView):

    def get(self, request, stockpk, risefall, timeindex):
        if (stock.objects.filter(pk=stockpk).exists()):
            stocking = stock.objects.get(pk=stockpk)
            list = stock_random_risefall_list.objects.get(stockname=stocking, index=int(timeindex))
            list.risefall = int(risefall)
            list.save()
            unicode_stockname = str(stocking.stock_name)
            success_change_response = u'成功更改股票' + unicode_stockname + u'的下次漲跌!\n'
            return HttpResponse(success_change_response)
        else:
            stock_nonexist_response = u'股票不存在!\n'
            return HttpResponse(stock_nonexist_response)

class generate_stock_risefall(APIView):

    def get(self, request):
        for i in range(1,7):
            stocking = stock.objects.get(pk=i)
            for j in range(1,31):
                if(stock_random_risefall_list.objects.filter(Q(stockname=stocking) & Q(index=j)).exists()):
                    a = stock_random_risefall_list.objects.get(stockname=stocking, index=j)
                    a.risefall = randint(-7,7)
                    a.save()
                else:
                    b = stock_random_risefall_list.objects.create(stockname=stocking, index=j)
                    b.risefall = randint(-7,7)
                    b.save()

        succes_response = u'成功建立股票漲幅表!'
        return HttpResponse(succes_response)

class stock_value_update(APIView):

    def get(self, request, timeindex):
        for i in range(1, 7):
            stocking = stock.objects.get(pk=i)
            a = stock_random_risefall_list.objects.get(stockname=stocking, index=timeindex)
            percentage = 0.01 * a.risefall
            new_value = float(stocking.stock_value) * (1.0 + percentage)
            stocking.stock_value = int(new_value)
            stocking.save()
            success_stock_value_update_response = u'成功更新當前股票價值\n'
            return HttpResponse(success_stock_value_update_response)

'''request part'''

#player
class request_bank_money(APIView):
    def get(self, request, playerpk):
        a = player.objects.get(pk = playerpk)
        response = str(a.bank_money)
        return HttpResponse(response)

class request_pocket_money(APIView):
    def get(self, request, playerpk):
        a = player.objects.get(pk = playerpk)
        response = str(a.pocket_money)
        return HttpResponse(response)

class request_knives(APIView):
    def get(self, request, playerpk):
        a = player.objects.get(pk = playerpk)
        response = str(a.poisoned)
        return HttpResponse(response)

#stock
class request_stock_amount(APIView):
    def get(self, request, stockpk, playerpk):
        stocking = stock.objects.get(pk=stockpk)
        user = player.objects.get(pk=playerpk)
        stock_record = players_stock_list.objects.get(owned_player=user, stock=stocking)
        response = str(stock_record.stock_amount)
        return HttpResponse(response)

class request_stock_value(APIView):
    def get(self, request, stockpk):
        stocking = stock.objects.get(pk=stockpk)
        response = str(stocking.stock_value)
        return HttpResponse(response)

class request_stock_last_risefall(APIView):
    def get(self, request, stockpk, timeindex):
        stocking = stock.objects.get(pk=stockpk)
        a = stock_random_risefall_list.objects.get(stockname=stocking, index=timeindex)
        response = str(a.risefall)
        return HttpResponse(response)

#land and houses
class request_lands(APIView):

    def get(self, request, playerpk, landpk):
        landing = land.objects.get(pk=landpk)
        if (int(landing.owner.player_number) == int(playerpk)):
            true_response = str(1)
            return  HttpResponse(true_response)
        else:
            false_response = str(0)
            return HttpResponse(false_response)

class request_houses(APIView):

    def get(self, request, landpk):
        landing = land.objects.get(pk=landpk)
        houses_response = str(landing.houses)
        return HttpResponse(houses_response)
'''

def Stock_Ups_And_Downs():              #定時更新股票價值
    for i in range(1, 7):
        stocking = stock.objects.get(pk=i)
        if (stocking.is_controlled):
            precentage1 = 0.01*float(stocking.controlled_ups_and_downs)
            new_value = float(stocking.stock_value) * (1.0 + precentage1)
            stocking.stock_value = int(new_value)
            stocking.is_controlled = False
            stocking.last_ups_and_downs = stocking.controlled_ups_and_downs
            stocking.save()
        else:
            rand = randint(0, 14) - 7
            precentage2 = 0.01 * float(rand)
            new_value = float(stocking.stock_value) * (1.0 + precentage2)
            stocking.stock_value = int(new_value)
            stocking.last_ups_and_downs = rand
            stocking.save()

def Knife_Damage():
    for i in range(1, 9):
        user = player.objects.get(pk=i)
        if (user.bank_money < 50):    #50為刀子傷害
            user.bank_money = 1      #不會導致破產
            user.save()
        else:
            user.bank_money -= 50
            user.save()

'''










