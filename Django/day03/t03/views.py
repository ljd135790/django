from django.shortcuts import render
from django.db.models import Avg
from .models import Player,Team

# Create your views here.

def get_player_avg_age(res):
    #拿国家队的数据
    players = Player.objects.filter(team__name="国家队")
    #求年纪平均
    res = players.aggregate(Avg("age"))
    print(res)