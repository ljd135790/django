from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="队名"
    )
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    age = models.IntegerField(
        verbose_name="年纪"
    )
    is_live = models.BooleanField(
        verbose_name="是否现役"
    )
    team = models.ForeignKey(
        Team,
        null=True,
        verbose_name="归属球队"
    )
    def __str__(self):
        return self.name