#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


class Stats(object):

    def __init__(self):
        pass

    @classmethod
    def ip(cls, ip_outs):
        """
        Inning Pitched
        :param ip_outs: inning pitched outs
        :return: (float) ip
        """
        return round(ip_outs / 3, 1)

    @classmethod
    def era(cls, er, ip):
        """
        Earned run average
        :param er: earned run
        :param ip: inning pitched
        :return: (float) era
        """
        return round((9 * er) / ip, 2)

    @classmethod
    def whip(cls, bb, h, ip):
        """
        Walks + Hits / IP
        :param bb: base on ball
        :param h: hits
        :param ip: inning pitched
        :return: (float) whip
        """
        return round((bb + h) / ip, 2)

    @classmethod
    def h9(cls, h, ip):
        """
        Hits / 9
        :param h: hits
        :param ip: inning pitched
        :return: (float) h9
        """
        return round((9 * h) / ip, 3)

    @classmethod
    def bb9(cls, bb, ip):
        """
        BB / 9
        :param bb: base on ball
        :param ip: inning pitched
        :return: (float) b9
        """
        return round((9 * bb) / ip, 3)

    @classmethod
    def hr9(cls, hr, ip):
        """
        HR / 9
        :param hr: home run
        :param ip: inning pitched
        :return: (float) hr9
        """
        return round((9 * hr) / ip, 3)

    @classmethod
    def single(cls, h, hr, _2b, _3b):
        """
        Single hits
        :param h: hits(all)
        :param hr: home run
        :param _2b: double
        :param _3b: triple
        :return: (int)single hits
        """
        return h - (hr + _2b + _3b)

    @classmethod
    def tb(cls, single, hr, _2b, _3b):
        """
        Total bases
        :param single: single hits
        :param hr: home run
        :param _2b: double
        :param _3b: triple
        :return: (int)total bases
        """
        return hr * 4 + _3b * 3 + _2b * 2 + single

    @classmethod
    def avg(cls, h, ab):
        """
        Batting average
        :param h: hits
        :param ab: at bat
        :return: (float)avg
        """
        return round(h / ab, 3)

    @classmethod
    def slg(cls, tb, ab):
        """
        Slugging
        :param tb: total bases
        :param ab: at bat
        :return: (float)slugging
        """
        return round(tb / ab, 3)

    @classmethod
    def obp(cls, h, bb, hbp, ab, sf):
        """
        On base percentage
        :param h: hits
        :param bb: base on ball
        :param hbp: hit by pitch
        :param ab: at bat
        :param sf: sacrifice fly
        :return: (float)obp
        """
        return round((h + bb + hbp) / (ab + bb + hbp + sf), 3)

    @classmethod
    def ops(cls, obp, slg):
        """
        On the base + slugging
        :param obp: on the base
        :param slg: slugging
        :return: (float) ops
        """
        return obp + slg
