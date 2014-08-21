#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


from script.tables import Team


class SabrMetrics(object):

    OUTPUT_DATA_TYPE_JSON = 'json'
    OUTPUT_DATA_TYPE_FLAME = 'flame'

    def __init__(self, session=None):
        # パスとか設定
        self.session = session

    def get_pytagorian__filter_by_league(self, year, lg, data_type=OUTPUT_DATA_TYPE_JSON):
        """

        :param year: year(required)
        :param lg: league(required)
        :param data_type: output data type(default:json)
        :return:
        """
        return self._get_pytagorian(
            self.session.query(Team).filter(
                and_(
                    Team.yearID == year,
                    Team.lgID == lg,
                )
            )
        )

    def get_pytagorian__filter_by_team(self, year, lg, team, data_type=OUTPUT_DATA_TYPE_JSON):
        """
        ピタゴラス勝率を求める
        :param year: year(required)
        :param lg: league(required)
        :param team: team name(required)
        :param data_type: output data type(default:json)
        :return:
        """
        return self._get_pytagorian(
            self.session.query(Team).filter(
                and_(
                    Team.yearID == year,
                    Team.lgID == lg,
                    Team.teamID == team,
                )
            )
        )

    def _get_pytagorian(self, values, data_type=OUTPUT_DATA_TYPE_JSON):
        """
        ピタゴラス勝率を求める
        :param values: year(required)
        :param lg: league(default:None(All))
        :param team: team name(prefix, default:None(All))
        :param data_type: output data type(default:json)
        :return:
        """
        # get team data
        for row in values.order_by(
            Team.yearID.asc(),
            Team.lgID.asc(),
            Team.divID.asc(),
            Team.Rank.asc()
        ).all():
            value = {'year': row.yearID, 'team': row.teamID, 'W': row.W, 'L': row.L}
            pytagorian_win = self._calc_pytagorian(row.R, row.ER)
            value['pytagorian'] = pytagorian_win
            print(value)

        if data_type == SabrMetrics.OUTPUT_DATA_TYPE_JSON:
            return {}
        elif data_type == SabrMetrics.OUTPUT_DATA_TYPE_FLAME:
            return []
        else:
            return {}

    def _calc_pytagorian(self, r, er):
        """
        ピタゴラス勝率計算
        :param r: 得点
        :param er: 失点
        :return: ピタゴラス勝率(float)
        """
        return (r ** 2) / ((r ** 2) + (er ** 2))


from sqlalchemy import *
from sqlalchemy.orm import *

from script.database_config import CONNECTION_TEXT, ENCODING


def main():
    engine = create_engine(CONNECTION_TEXT, encoding=ENCODING)
    Session = sessionmaker(bind=engine, autoflush=True)
    Session.configure(bind=engine)
    lh = SabrMetrics(session=Session())
    values = lh.get_pytagorian__filter_by_league(2013, 'AL')
    values = lh.get_pytagorian__filter_by_team(2011, 'AL', 'OAK')


if __name__ == '__main__':
    main()