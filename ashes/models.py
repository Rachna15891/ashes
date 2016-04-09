from django.db import models

class PlayerStats(models.Model):
    total_runs = models.IntegerField(default=0, null=True)
    total_outs = models.IntegerField(default=0, null=True)
    innings = models.IntegerField(default=0, null=True)
    player_name = models.CharField(max_length=150, primary_key=True)
    batting_impact_list = models.CharField(max_length=500, null=True)
    runs_in_matches = models.CharField(max_length=500, null=True)
    tag = models.CharField(max_length=50, null=True)
    batting_avg = models.FloatField(default=0, null=True)
    caa = models.FloatField(default=0, null=True)
    last_bat_impact = models.FloatField(default=0, null=True)
    team_name = models.CharField(max_length=100, null=True)