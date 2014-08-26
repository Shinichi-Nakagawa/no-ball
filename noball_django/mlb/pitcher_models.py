#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


from django.db import models


class Pitching(models.Model):
    """
    Pitching stats
    """

    playerID = models.CharField(max_length=9, primary_key=True, null=False)
    yearID = models.IntegerField(max_length=11, primary_key=True, null=False)
    stint = models.IntegerField(max_length=11, primary_key=True, null=False)
    teamID = models.CharField(max_length=3)
    lgID = models.CharField(max_length=2)
    W = models.IntegerField(max_length=11)
    L = models.IntegerField(max_length=11)
    G = models.IntegerField(max_length=11)
    GS = models.IntegerField(max_length=11)
    CG = models.IntegerField(max_length=11)
    SHO = models.IntegerField(max_length=11)
    SV = models.IntegerField(max_length=11)
    IPouts = models.IntegerField(max_length=11)
    H = models.IntegerField(max_length=11)
    ER = models.IntegerField(max_length=11)
    HR = models.IntegerField(max_length=11)
    BB = models.IntegerField(max_length=11)
    SO = models.IntegerField(max_length=11)
    BAOpp = models.FloatField()
    ERA = models.FloatField()
    IBB = models.IntegerField(max_length=11)
    WP = models.IntegerField(max_length=11)
    HBP = models.IntegerField(max_length=11)
    BK = models.IntegerField(max_length=11)
    BFP = models.IntegerField(max_length=11)
    GF = models.IntegerField(max_length=11)
    R = models.IntegerField(max_length=11)
    SH = models.IntegerField(max_length=11)
    SF = models.IntegerField(max_length=11)
    GIDP = models.IntegerField(max_length=11)

    def ip(self, ):
        """
        Inning Pitched
        :return: (float)ip
        """
        return float(self.IPouts / 3, 3)

    def whip(self, ):
        """
        Walks + Hits / IP
        :return: (float)whip
        """
        return round((self.BB + self.H) / self.ip(), 3)

    def h9(self, ):
        """
        Hits / 9
        :return:(float)h9
        """
        return round((9 * self.H) / self.ip(), 3)

    def bb9(self ,):
        """
        BB / 9
        :return:(float)bb9
        """
        return round((9 * self.BB) / self.ip(), 3)

    def hr9(self, ):
        """
        HR / 9
        :return:(float)hr9
        """
        return round((9 * self.HR) / self.ip(), 3)

    class Meta():
        db_table = 'Pitching'
