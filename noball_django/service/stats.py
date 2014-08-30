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
    def so9(cls, so, ip):
        """
        Strike out / 9
        :param so: strike out
        :param ip: inning pitched
        :return: (float) so9
        """
        return round((9 * so) / ip, 3)

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

    @classmethod
    def babip(cls, h, hr, ab, so, sf):
        """
        Batting average on balls in play(BABIP)
        :param h: hits
        :param hr: home run
        :param ab: at bat
        :param so: strike out
        :param sf: sacrifice fly
        :return: (float) babip
        """
        return round((h - hr) / (ab - so - hr + sf), 3)

    @classmethod
    def rc(cls, h, bb, hbp, cs, gidp, tb, sf, sh, sb, so, ab):
        """
        Runs created
        :param h: hits
        :param bb: base on ball
        :param hbp: hit by pitch
        :param cs: caught stealing
        :param gidp: ground into duble play
        :param tb: total bases
        :param sf: sacrifice fly
        :param sh: sacrifice hit
        :param sb: stolen base
        :param so: strike out
        :param ab: at bat
        :return: (float) run created
        """
        # (出塁能力A * 進塁能力B) / 出塁機会C
        a = float(h + bb + hbp - cs - gidp)
        b = float(tb + 0.26 * (bb + hbp) + 0.53 * (sf + sh) + 0.64 * sb - 0.03 * so)
        c = ab + bb + hbp + sf + sh
        return float(((a + 2.4 * c) * (b + 3 * c)/9 * c) - 0.9 * c)

    @classmethod
    def rc27(cls, rc, ab, h, sh, sf, cs, gidp):
        """
        Runs created 27
        :param rc: run created
        :param ab: at bat
        :param h: hits
        :param sh: sacrifice hit
        :param sf: sacrifice fly
        :param cs: caught stealing
        :param gidp: ground into duble play
        :return: (float) run created 27
        """
        to = ab - h + sh + sf + cs + gidp
        return float(27 * rc / to)