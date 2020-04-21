#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def main(src_file, dst_file=''):
    with open(src_file) as f:
        lines = f.readlines()
    pid = 0
    for i, text in enumerate(lines):
        if len(re.findall('<p', text)) > 1:
            print('Line %d has multiple <p>' % (i + 1))
            return
        if re.search('<p[> ]', text):
            pid += 1
            lines[i] = re.sub("<p( id='.+')", "<p id='p%d'" % pid, text)
    print('%d ids added' % pid)
    with open(dst_file or src_file, 'w') as f:
        f.writelines(lines)


if __name__ == '__main__':
    import fire

    fire.Fire(main)
