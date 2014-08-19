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
        self.module = __import__(JsonToMySQL.BASE_MODULE, globals(), locals(), [], 0)
        self.session = session

    def run(self):
        """
        実行
        """
        print('Open database connection')

        for json_file in self.json_files:
            root, ext = os.path.splitext(json_file)
            # json file open
            print('create for %s' % root)
            json_file_fullpath = os.path.join(self.data_path, json_file)
            print('for row in rows')
            fp = open(json_file_fullpath, mode='r')
            cls = self._get_class(root)

            # get model class
            self._save_rows(json.load(fp), cls)

        print('Close database connection')

    def _get_class(self, base_name):
        """
        JSON file name to class
        :param base_name: JSON file name(base)
        :return: SQLAlchemy Model class
        """
        # 名前が複数形の場合は単数形にして取得
        if 'ies' in base_name:
            class_name = re.sub(r'ies$', 'y', base_name)
        else:
            class_name = re.sub(r's$', '', base_name)
        return getattr(self.module, class_name)

    def _save_rows(self, rows, cls):
        """
        テーブルに保存
        :param rows: json records
        :param cls: SQLAlchemy Model class
        :return: None
        """
        for row in rows:
            model = self._get_model(row, cls)

    def _get_model(self, values, cls):
        """
        内容を詰める
        :param value:
        :param cls:
        :return: model
        """
        model = cls()
        for k, v in values.items():
            if k in dir(model):
                setattr(model, k, v)

        return model


def main(path):
    lh = JsonToMySQL(base_path=path, session=None)
    lh.run()


if __name__ == '__main__':
    base_path = os.path.dirname(__file__).replace('script', JsonToMySQL.BASE_DIR)
    main(base_path)
