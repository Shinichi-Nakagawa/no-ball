#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
選手の情報に関する振る舞いを提供するService
"""

import locale

from noball_django.settings import APPLICATION_NAME


__author__ = 'shinyorke'


class MLBService(object):

    # サブドメイン名
    SUB_DOMAIN = 'mlb'
    # Queryのキー名
    QUERY_KEY = 'query_word'

    # Playerの区分(野手or投手)
    PLAYER_BATTER = 'b'
    PLAYER_PITCHER = 'p'

    # 右/左/両の略称
    SHORT_NAME_RIGHT = 'R'
    SHORT_NAME_LEFT = 'L'
    SHORT_NAME_SWITCH = 'S'

    # 通貨記号（アメリカなので＄）
    CURRENCY = '$'
    # SALARYの分母(million)
    BASE_SALARY = 1000000

    # ピタゴラス勝率のべき乗
    PYTHAGORIAN_POWER = 2

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
            'PLAYER_BATTER': MLBService.PLAYER_BATTER,
            'PLAYER_PITCHER': MLBService.PLAYER_PITCHER,
            'MENU_ENABLE': True,
        }

    def get_pythagoras_dataset(self, teams):
        """
        ピタゴラス勝率を含んだデータセットを返す
        :param teams: Team Model List
        :return: pythagoras % list
        """
        datasets = [
            {
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
             for t in teams
        ]
        return datasets

    @classmethod
    def calc_winning_percentage(cls, w, g):
        """
        勝率
        :param w: win
        :param g: games
        :return: winning percentage
        """
        return w / g

    @classmethod
    def calc_pythagorean_expectation(cls, r, ra):
        """
        ピタゴラス勝率
        :param r: Runs Scored
        :param ra: Runs Allowed
        :return: pythagorean expectation
        """
        r_power = r ^ MLBService.PYTHAGORIAN_POWER
        ra_power = ra ^ MLBService.PYTHAGORIAN_POWER
        return r_power / (r_power + ra_power)

