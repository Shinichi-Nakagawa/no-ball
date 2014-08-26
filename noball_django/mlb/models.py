
# Create your models here.
from django.db import models


class Master(models.Model):
    """
    Player profile
    """

    playerID = models.CharField(max_length=9, primary_key=True, default='', null=False)
    hofID = models.CharField(max_length=10)
    birthYear = models.IntegerField(max_length=11)
    birthMonth = models.IntegerField(max_length=11)
    birthDay = models.IntegerField(max_length=11)
    birthCountry = models.CharField(max_length=50)
    birthState = models.CharField(max_length=2)
    birthCity = models.CharField(max_length=50)
    deathYear = models.IntegerField(max_length=11)
    deathMonth = models.IntegerField(max_length=11)
    deathDay = models.IntegerField(max_length=11)
    deathCountry = models.CharField(max_length=50)
    deathState = models.CharField(max_length=2)
    deathCity = models.CharField(max_length=50)
    nameFirst = models.CharField(max_length=50)
    nameLast = models.CharField(max_length=50)
    nameNote = models.CharField(max_length=255)
    nameGiven = models.CharField(max_length=255)
    nameNick = models.CharField(max_length=255)
    weight = models.IntegerField(max_length=11)
    height = models.FloatField()
    bats = models.CharField(max_length=1)
    throws = models.CharField(max_length=1)
    debut = models.CharField(max_length=10)
    finalGame = models.CharField(max_length=10)
    college = models.CharField(max_length=50)
    lahman40ID = models.CharField(max_length=9)
    lahman45ID = models.CharField(max_length=9)
    retroID = models.CharField(max_length=9)
    holtzID = models.CharField(max_length=9)
    bbrefID = models.CharField(max_length=9)

    class Meta():
        db_table = 'Master'


class Salary(models.Model):
    """
    Player Salary
    """
    yearID = models.IntegerField(max_length=11, primary_key=True, null=False)
    teamID = models.CharField(max_length=3, primary_key=True, null=False)
    lgID = models.CharField(max_length=2, primary_key=True, null=False)
    playerID = models.CharField(max_length=9, primary_key=True, null=False)
    salary = models.FloatField()

    class Meta():
        db_table = 'Salaries'


class Team(models.Model):
    """
    Team stats
    """

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

    class Meta():
        db_table = 'Teams'
