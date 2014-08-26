#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


from django.db import models


class Batting(models.Model):
    """
    Batting stats
    """

    playerID = models.CharField(max_length=9, primary_key=True, null=False)
    yearID = models.IntegerField(max_length=11, primary_key=True, null=False)
    stint = models.IntegerField(max_length=11, primary_key=True, null=False)
    teamID = models.CharField(max_length=3)
    lgID = models.CharField(max_length=2)
    G = models.IntegerField(max_length=11)
    G_batting = models.IntegerField(max_length=11)
    AB = models.IntegerField(max_length=11)
    R = models.IntegerField(max_length=11)
    H = models.IntegerField(max_length=11)
    _2B = models.IntegerField(max_length=11, db_column='2B')
    _3B = models.IntegerField(max_length=11, db_column='3B')
    HR = models.IntegerField(max_length=11)
    RBI = models.IntegerField(max_length=11)
    SB = models.IntegerField(max_length=11)
    CS = models.IntegerField(max_length=11)
    BB = models.IntegerField(max_length=11)
    SO = models.IntegerField(max_length=11)
    IBB = models.IntegerField(max_length=11)
    HBP = models.IntegerField(max_length=11)
    SH = models.IntegerField(max_length=11)
    SF = models.IntegerField(max_length=11)
    GIDP = models.IntegerField(max_length=11)
    G_old = models.IntegerField(max_length=11)

    class Meta():
        db_table = 'Batting'
