#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@desc: 从注解网页中提取段落中的原文与注解
@file: extract_for_merge.py
@time: 2020-07-25
"""
import re
import json


def extract(html_file, out_file):
    rows = open(html_file).readlines()
    rows = [(i, re.search(r'<b class="ori">(.+?)</b>', r).group(1),
             re.search(r'</b>　(.+?)</p>', r).group(1))
            for i, r in enumerate(rows) if '<b class="ori">' in r and '　' in r]
    with open(out_file, 'w') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    extract('/Users/zyg/Desktop/lq/cb-study/T1850.html', 'T1850.json.js')
