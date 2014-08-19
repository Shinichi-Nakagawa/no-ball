#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
jsonからMySQLに保存
"""
__author__ = 'Shinichi Nakagawa'

import os
import json
import re
import tables


class JsonToMySQL(object):
    BASE_DIR = 'data'
    JSON_DATA_DIR = 'output'
    ENCODING = 'utf-8'
    BASE_MODULE = 'tables'

    def __init__(self, base_path='', session=None):
        # パスとか設定
        self.base_path = base_path
        self.data_path = os.path.join(self.base_path, self.JSON_DATA_DIR)
        self.json_files = os.listdir(self.data_path)
        self.session = session

    def run(self):
        """
        実行
        """
        print('Get module')
        module = __import__(JsonToMySQL.BASE_MODULE, globals(), locals(), [], 0)
        print('Open database connection')

        for json_file in self.json_files:
            root, ext = os.path.splitext(json_file)
            # json file open
            print('create for %s' % root)
            json_file_fullpath = os.path.join(self.data_path, json_file)
            print('for row in rows')
            fp = open(json_file_fullpath, mode='r')
            # get cls
            if 'ies' in root:
                class_name = re.sub(r'ies$', 'y', root)
            else:
                class_name = re.sub(r's$', '', root)
            cls = getattr(module, class_name)
            print(cls)
            print(dir(cls))

            # get model class
            self._save_rows(json.load(fp))

        print('Close database connection')

    def _save_rows(self, rows):
        """
        テーブルに保存
        :param rows: json records
        :return: None
        """
        for row in rows:
            pass
            # print(row)


def main(path):
    lh = JsonToMySQL(base_path=path, session=None)
    lh.run()


if __name__ == '__main__':
    base_path = os.path.dirname(__file__).replace('script', JsonToMySQL.BASE_DIR)
    main(base_path)
