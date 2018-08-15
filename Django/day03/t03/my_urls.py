from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^get_player_v1$",get_player_avg_age)
]
