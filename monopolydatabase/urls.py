"""monopolydatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import Addmoney_bank,Addmoney_pocket, Got_knife, Cure_knife, Got_land, Get_house, stockss, change_stock_risefall, generate_stock_risefall, stock_value_update, request_bank_money, request_pocket_money, request_knives, request_stock_amount, request_stock_value, request_stock_last_risefall, request_lands, request_houses

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^addmoney-bank/(?P<recieverpk>\d+)/(?P<money>-?\d+)/$', Addmoney_bank.as_view()),                                     #銀行加錢或扣錢 addmoney-bank/小隊編號/錢的數量(可以是負的變扣錢)/
    url(r'^addmoney-pocket/(?P<recieverpk>\d+)/(?P<money>-?\d+)/$', Addmoney_pocket.as_view()),                                 #現金加錢或扣錢 addmoney-pocket/小隊編號/錢的數量(可以是負的變扣錢)/
    url(r'^knife/(?P<recieverpk>\d+)/$', Got_knife.as_view()),                                                                  #接受刀傷 knife/小隊編號/      :直接預設+1刀傷
    url(r'^cure-knife/(?P<recieverpk>\d+)/$', Cure_knife.as_view()),                                                            #醫院治療刀傷 cure-knife/小隊編號/    :直接治療所有刀傷
    url(r'^get-or-loss-land/(?P<playerpk>\d+)/(?P<landpk>\d+)/(?P<get_or_loss>\d+)/$', Got_land.as_view()),                     #買土地(包含扣錢)或無償失去土地 get-or-loss-land/小隊編號/土地編號/買或失去(只允許0或1，0=失去; 1=購買，若為其他值皆當作失去。失去土地不會得到錢)/
    url(r'^add-house/(?P<playerpk>\d+)/(?P<landpk>\d+)/(?P<amount>-?\d+)/$', Get_house.as_view()),                              #買房(不包含扣錢)或無償拆房 add-house/小隊編號/土地編號/房子數量(負值為拆房)/    買房子不扣錢請搭配扣錢函式使用，拆房子不會得到錢
    url(r'^sell-stock/(?P<playerpk>\d+)/(?P<stockpk>\d+)/(?P<amount>-?\d+)/$', stockss.as_view()),                              #買賣股票(包含加扣錢) sell-stock/小隊編號/股票編號/數量(負值為賣出)/
    url(r'^change-stock-risefall/(?P<stockpk>\d+)/(?P<risefall>-?\d+)/(?P<timeindex>\d+)/$', change_stock_risefall.as_view()),  #改變特定股票的漲幅 change-stock-risefall/股票編號/要改的漲幅(可以是負的)/時間index(1為第一個5分鐘第一次改，上限為30)/
    url(r'^genertate-stock-risefall/$', generate_stock_risefall.as_view()),                                                     #跑出股票漲幅表 genertate-stock-risefall/          產生所有股票未來的所有漲幅
    url(r'^periodic-update-stock-value/(?P<timeindex>\d+)/$', stock_value_update.as_view()),                                    #根據漲幅表更改股票的市值 periodic-update-stock-value/時間index(1為第一個5分鐘第一次改，上限為30)/   自動根據時間index的時間找出漲幅表的資料更改所有股票的市值

    url(r'^request-bank-money/(?P<playerpk>\d+)/$', request_bank_money.as_view()),                                              #獲得小隊的銀行金額 request-bank-money/小隊編號
    url(r'^request-pocket-money/(?P<playerpk>\d+)/$', request_pocket_money.as_view()),                                          #獲得小隊的現金金額 request-pocket-money/小隊編號
    url(r'^request-knives/(?P<playerpk>\d+)/$', request_knives.as_view()),                                                      #獲得小隊的刀傷數量 request-knives/小隊編號

    url(r'^request-stock-amount/(?P<stockpk>\d+)/(?P<playerpk>\d+)/$', request_stock_amount.as_view()),                         #獲得某小隊持有某股票的數量 request-stock-amount/股票編號/小隊編號/
    url(r'^request-stock-value/(?P<stockpk>\d+)/$', request_stock_value.as_view()),                                             #獲得某股票的市值 request-stock-value/股票編號
    url(r'^request-stock-last-risefall/(?P<stockpk>\d+)/(?P<timeindex>\d+)/$', request_stock_last_risefall.as_view()),          #獲得某股票特定時間的漲幅 request-stock-last-risefall/股票編號/(1為第一個5分鐘第一次改，上限為30)/

    url(r'^request-lands/(?P<playerpk>\d+)/(?P<landpk>\d+)/$', request_lands.as_view()),                                        #判斷特定土地是否為特定小隊擁有 request-lands/小隊編號/土地編號        回傳1=True(擁有) 0=False(不擁有)
    url(r'^request-houses/(?P<landpk>\d+)/$', request_houses.as_view()),                                                        #獲得特定土地的房子數量 request-houses/土地編號
]