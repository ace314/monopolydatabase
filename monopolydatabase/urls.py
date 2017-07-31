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
    url(r'^addmoney-bank/(?P<recieverpk>\d+)/(?P<money>-?\d+)/$', Addmoney_bank.as_view()),
    url(r'^addmoney-pocket/(?P<recieverpk>\d+)/(?P<money>-?\d+)/$', Addmoney_pocket.as_view()),
    url(r'^knife/(?P<recieverpk>\d+)/$', Got_knife.as_view()),
    url(r'^cure-knife/(?P<recieverpk>\d+)/$', Cure_knife.as_view()),
    url(r'^get-or-loss-land/(?P<playerpk>\d+)/(?P<landname>[-\w]+)/(?P<get_or_loss>\d+)/$', Got_land.as_view()),
    url(r'^add-house/(?P<playerpk>\d+)/(?P<landname>[-\w]+)/(?P<amount>-?\d+)/$', Get_house.as_view()),
    url(r'^sell-stock/(?P<playerpk>\d+)/(?P<stockname>[-\w]+)/(?P<amount>-?\d+)/$', stockss.as_view()),
    url(r'^change-stock-risefall/(?P<stockname>[-\w]+)/(?P<risefall>-?\d+)/(?P<timeindex>\d+)/$', change_stock_risefall.as_view()),
    url(r'^genertate-stock-risefall/$', generate_stock_risefall.as_view()),
    url(r'^periodic-update-stock-value/(?P<timeindex>\d+)/$', stock_value_update.as_view()),

    url(r'^request-bank-money/(?P<playerpk>\d+)/$', request_bank_money.as_view()),
    url(r'^request-pocket-money/(?P<playerpk>\d+)/$', request_pocket_money.as_view()),
    url(r'^request-knives/(?P<playerpk>\d+)/$', request_knives.as_view()),

    url(r'^request-stock-amount/(?P<stockname>[-\w]+)/(?P<playerpk>\d+)/$', request_stock_amount.as_view()),
    url(r'^request-stock-value/(?P<stockname>[-\w]+)/$', request_stock_value.as_view()),
    url(r'^request-stock-last-risefall/(?P<stockname>[-\w]+)/(?P<timeindex>\d+)/$', request_stock_last_risefall.as_view()),

    url(r'^request-lands/(?P<playerpk>\d+)/(?P<landpk>\d+)/$', request_lands.as_view()),
    url(r'^request-houses/(?P<landname>[-\w]+)/$', request_houses.as_view()),
]