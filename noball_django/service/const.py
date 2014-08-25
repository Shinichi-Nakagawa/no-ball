#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
serviceの定数クラス
"""
__author__ = 'Shinichi Nakagawa'

PLAYERS_NAME_DELI = " "
PLAYERS_PAGE_URL = 'http://www.baseball-reference.com/players/%(letter)s/'
PLAYERS_PAGE_URL_SUFIX_BATTER = "-bat.shtml"
PLAYERS_PAGE_URL_SUFIX_PITCHER = "-pitch.shtml"
PLAYERS_PAGE_URL_SUFIX_REPLACE = ".shtml"

MAX_YEAR = 2013
LEAGUE_AL = 'AL'
LEAGUE_NL = 'NL'
LEAGUES = (LEAGUE_AL, LEAGUE_NL)
LEAGUE_TUPLES = (
    (LEAGUE_AL, LEAGUE_AL),
    (LEAGUE_NL, LEAGUE_NL)
)

STANDARD_BATTING_COLUMNS = (
'Year',
'Age',
'Team',
'League',
'G',
'PA',
'AB',
'R',
'H',
'2B',
'3B',
'HR',
'RBI',
'SB',
'CS',
'BB',
'SO',
'BA',
'OBP',
'SLG',
'OPS',
'OPS+',
'TB',
'GDP',
'HBP',
'SH',
'SF',
'IBB',
'Pos',
'Awards'
)
VALUE_BATTING_COLUMNS = (
'Year',
'Age',
'Team',
'Lg',
'G',
'PA',
'Rbat',
'Rbaser',
'Rdp',
'Rfield',
'Rpos',
'RAA',
'WAA',
'Rrep',
'RAR',
'WAR',
'waaWL%',
'162WL%',
'oWAR',
'dWAR',
'oRAR',
'Salary',
'Pos',
'Awards'
)

STANDARD_PITCHING_COLUMNS = (
'Year',
'Age',
'Team',
'League',
'W',
'L',
'W-L%',
'ERA',
'G',
'GS',
'GF',
'CG',
'SHO',
'SV',
'IP',
'H',
'R',
'ER',
'HR',
'BB',
'IBB',
'SO',
'HBP',
'BK',
'WP',
'BF',
'ERA+',
'WHIP',
'H9',
'HR9',
'BB9',
'SO9',
'SOBB',
'Awards'
)

ADVANCED_COLUMNS = (
'Year',
'Age',
'Team',
'Lg',
'PA',
'Outs',
'RC',
'RC/G',
'AIR',
'BAbip',
'BA',
'lgBA',
'OBP',
'lgOBP',
'SLG',
'lgSLG',
'OPS',
'lgOPS',
'OPS+',
'OWn%',
'BtRuns',
'BtWins',
'TotA',
'SecA',
'ISO',
'PwrSpd'
)

VALUE_PITCHING_COLUMNS =(
'Year',
'Age',
'Team',
'Lg',
'IP',
'G',
'GS',
'R',
'RA9',
'RA9opp',
'RA9def',
'RA9role',
'PPFp',
'RA9avg',
'RAA',
'WAA',
'gmLI',
'WAAadj',
'WAR',
'RAR',
'waaWL%',
'162WL%',
'Salary',
'Awards'
)

PITCHING_BATTING_COLUMNS = (
'Year',
'Age',
'Team',
'Lg',
'PAu',
'G',
'PA',
'AB',
'R',
'H',
'2B',
'3B',
'HR',
'SB',
'CS',
'BB',
'SO',
'BA',
'OBP',
'SLG',
'OPS',
'BAbip',
'TB',
'GDP',
'HBP',
'SH',
'SF',
'IBB',
'ROE'
)

PITCHING_STANDARD_TABLE = "pitching_standard"
PITCHING_VALUE_TABLE = "pitching_value"
PITCHING_BATTING_TABLE = "pitching_batting"

BATTING_STANDARD_TABLE = "batting_standard"
BATTING_VALUE_TABLE = "batting_value"
BATTING_ADVANCED_TABLE = "batting_advanced"

RE_TEMPLATE = '%s\.((18|19|20)[0-9]{2})'

# ポジションFLG
POSITION_PITCHER = "p"
POSITION_BATTER = "b"

# ポジション辞書(Key:BRFの名称 Value:略称)
POSITION_DICT = {
    'Pitcher': 'P',  # 投手
    'SP': 'SP',  # 先発
    'RP': 'RP',  # リリーフ
    'CL': 'CL',  # 抑え
    'Catcher': 'C',  # 捕手
    'First Baseman': '1B',  # 一塁
    'Second Baseman': '2B',  # 二塁
    'Third Baseman': '3B',  # 三塁
    'Shortstop': 'SS',  # 遊撃手
    'Leftfielder': 'LF',  # 左翼
    'Centerfielder': 'CF',  # 中堅
    'Rightfielder': 'RF',  # 右翼
    'Outfielder': 'OF',  # 外野手全般
    'Designated Hitter': 'DH',  # 指名打者
    'Pinch Hitter': 'PH',  # 代打専門
}

# 右/左/両
HANDS_RIGHT = 'Right'
HANDS_LEFT = 'Left'
BATTING_SWITCH = 'Both'
