#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
選手の情報に関する振る舞いを提供するService
"""

import locale
from datetime import datetime

from service.const import POSITION_PITCHER, POSITION_BATTER
from noball_django.settings import APPLICATION_NAME


__author__ = 'shinyorke'


class MLBService(object):

    # サブドメイン名
    SUB_DOMAIN = 'mlb'
    # Queryのキー名
    QUERY_KEY = 'query_word'

    # 右/左/両の略称
    SHORT_NAME_RIGHT = 'R'
    SHORT_NAME_LEFT = 'L'
    SHORT_NAME_SWITCH = 'S'

    # 通貨記号（アメリカなので＄）
    CURRENCY = '$'
    # SALARYの分母(million)
    BASE_SALARY = 1000000

    # ピタゴラス勝率のべき乗
    PYTHAGORIAN_POWER = 1.8

    def __init__(self, encode):
        locale.setlocale(locale.LC_NUMERIC, encode)

    def get_base_context(self):
        """
        戻り値定数セット
        :return: 戻り値(固定)
        """
        return {
            'APPLICATION_NAME': APPLICATION_NAME,
            'QUERY_KEY': MLBService.QUERY_KEY,
            'SUB_DOMAIN': MLBService.SUB_DOMAIN,
            'PLAYER_BATTER': POSITION_BATTER,
            'PLAYER_PITCHER': POSITION_PITCHER,
            'MENU_ENABLE': True,
        }

    def get_pythagoras_dataset(self, teams):
        """
        ピタゴラス勝率を含んだデータセットを返す
        :param teams: Team Model List
        :return: pythagoras % list
        """
        datasets = []
        for t in teams:
            d = {
                'team': t.teamID,
                'name': t.name,
                'div': t.divID,
                'rank': t.Rank,
                'g': t.G,
                'w': t.W,
                'l': t.L,
                'r': t.R,
                'er': t.ER,
                'win_p': MLBService.calc_winning_percentage(t.W, t.G),
                'pyt_p': MLBService.calc_pythagorean_expectation(t.R, t.RA)
            }
            d['pyt_p_w'] = round(t.G * d['pyt_p'], 0)
            d['pyt_p_l'] = t.G - d['pyt_p_w']
            datasets.append(d)
        return datasets

    def get_home_value_pitcher(self, player, player_stats):
        """
        Pitcher profile
        :param player: Player stats
        :param player_stats: Player stats
        :return: pitcher profile(dict)
        """
        _prof = self._get_base_profile(player, player_stats)
        _prof['position'] = POSITION_PITCHER.upper()
        _prof['win'] = player_stats[0].W
        _prof['lose'] = player_stats[0].L
        _prof['era'] = player_stats[0].ERA
        _prof['so'] = player_stats[0].SO
        return _prof

    def get_home_value_batter(self, player, player_stats):
        """
        Batter profile
        :param player: Player stats
        :param player_stats: Player stats
        :return: batter profile(dict)
        """
        _prof = self._get_base_profile(player, player_stats)
        _prof['position'] = POSITION_BATTER.upper()
        _prof['avg'] = player_stats[0].avg()
        _prof['hr'] = player_stats[0].HR
        _prof['rbi'] = player_stats[0].RBI
        return _prof

    def _get_base_profile(self, player, player_stats):
        """
        Profile(Base)
        :param player: Player stats
        :param player_stats: Player stats
        :return: profile(dict)
        """
        return {
            'year': player_stats[0].yearID,
            'team': player_stats[0].teamID,
            'age': MLBService.calc_age(player.birthYear),
            'birthday': '%d/%d/%d' % (player.birthYear, player.birthMonth, player.birthDay),
            'salary': 'salary',
            'country': player.birthCountry,
            'city': player.birthCity,
            'bats': player.bats,
            'throws': player.throws

        }

    @classmethod
    def calc_age(cls, year):
        """
        calculate age
        :param year: (int)birth year
        :return: (int) age
        """
        now = datetime.now()
        return now.year - year

    @classmethod
    def calc_winning_percentage(cls, w, g):
        """
        勝率
        :param w: win
        :param g: games
        :return: winning percentage
        """
        return round(w / g, 3)

    @classmethod
    def calc_pythagorean_expectation(cls, r, ra):
        """
        ピタゴラス勝率
        :param r: Runs Scored
        :param ra: Runs Allowed
        :return: pythagorean expectation
        """
        r_power = r ** MLBService.PYTHAGORIAN_POWER
        ra_power = ra ** MLBService.PYTHAGORIAN_POWER
        return round(r_power / (r_power + ra_power), 3)

