#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

__author__ = 'Shinichi Nakagawa'


class SearchForm(forms.Form):
    player_name = forms.CharField(max_length=255)
