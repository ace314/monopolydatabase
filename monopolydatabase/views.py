from django.shortcuts import render
from rest_framework.views import APIView
from django.views.generic import ListView

from django.http import HttpResponse

from .models import player
# Create your views here.

class Give(APIView):

    def give_money(self, giverpk, recieverpk, money):
        giver = player.objects.get(pk=giverpk)
        reciever = player.objects.get(pk=recieverpk)
