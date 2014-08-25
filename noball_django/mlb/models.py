from django.db import models

# Create your models here.
import json
from django.db import models


class Team(models.Model):

    yearID = models.IntegerField(max_length=11, primary_key=True, null=False)
    lgID = models.CharField(max_length=2, primary_key=True, null=False)
    teamID = models.CharField(max_length=3, primary_key=True, null=False)
    franchID = models.CharField(max_length=3)
    divID = models.CharField(max_length=1)
    Rank = models.IntegerField(max_length=11)
    G = models.IntegerField(max_length=11)
    Ghome = models.IntegerField(max_length=11)
    W = models.IntegerField(max_length=11)
    L = models.IntegerField(max_length=11)
    DivWin = models.CharField(max_length=1)
    WCWin = models.CharField(max_length=1)
    LgWin = models.CharField(max_length=1)
    WSWin = models.CharField(max_length=1)
    R = models.IntegerField(max_length=11)
    AB = models.IntegerField(max_length=11)
    H = models.IntegerField(max_length=11)
    _2B = models.IntegerField(max_length=11, db_column='2B')
    _3B = models.IntegerField(max_length=11, db_column='3B')
    HR = models.IntegerField(max_length=11)
    BB = models.IntegerField(max_length=11)
    SO = models.IntegerField(max_length=11)
    SB = models.IntegerField(max_length=11)
    CS = models.IntegerField(max_length=11)
    HBP = models.IntegerField(max_length=11)
    SF = models.IntegerField(max_length=11)
    RA = models.IntegerField(max_length=11)
    ER = models.IntegerField(max_length=11)
    ERA = models.FloatField()
    CG = models.IntegerField(max_length=11)
    SHO = models.IntegerField(max_length=11)
    SV = models.IntegerField(max_length=11)
    IPouts = models.IntegerField(max_length=11)
    HA = models.IntegerField(max_length=11)
    HRA = models.IntegerField(max_length=11)
    BBA = models.IntegerField(max_length=11)
    SOA = models.IntegerField(max_length=11)
    E = models.IntegerField(max_length=11)
    DP = models.IntegerField(max_length=11)
    FP = models.FloatField()
    name = models.CharField(max_length=50)
    park = models.CharField(max_length=255)
    attendance = models.IntegerField(max_length=11)
    BPF = models.IntegerField(max_length=11)
    PPF = models.IntegerField(max_length=11)
    teamIDBR = models.CharField(max_length=3)
    teamIDlahman45 = models.CharField(max_length=3)
    teamIDretro = models.CharField(max_length=3)

    def get_profile_2_dict(self):
        """
        Profile(JSON) to Dictionary
        """
        return json.loads(self.profile)

    class Meta():
        db_table = 'Teams'