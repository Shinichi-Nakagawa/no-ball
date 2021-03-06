#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'

ENCODING = 'utf-8'

PARAMS = {
    'dialect': 'mysql',
    'driver': 'pymysql',
    'user': 'username',
    'password': 'password',
    'host': '192.168.33.10',
    'port': '3306',
    'database': 'sean_lahman'

}

CONNECTION_TEXT = "{dialect}+{driver}://{user}:{password}@{host}:{port}/{database}".format(**PARAMS)
