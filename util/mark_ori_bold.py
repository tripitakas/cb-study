#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@desc: 将从CB下载的注疏网页的论原文部分加粗，可加样式 `.ori {color: #009;}`
@file: mark_ori_bold.py
@time: 2020-07-25
"""
import re


def extract(html_file, out_file=None):
    rows = open(html_file).readlines()
    rows = [re.sub(r'</span>([^　]+)　', lambda m: m.group().replace(
        m.group(1), '<b class="ori">%s</b>' % m.group(1)), t) for t in rows]
    with open(out_file or html_file.replace('.html', '-.html'), 'w') as f:
        f.writelines(rows)


if __name__ == '__main__':
    import fire

    fire.Fire(extract)
