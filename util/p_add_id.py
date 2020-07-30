#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def main(src_file, dst_file=''):
    with open(src_file) as f:
        lines = f.readlines()
    pid = gid = 0
    juan_head = None
    for i, text in enumerate(lines):
        text = re.sub(r'^\s*No[.0-9 ]+(\[No[.0-9 ]+\])?<', '<', text)  # Remove `No. 1666 [No. 1667]`
        juan_name = re.findall("class='juan'>([^<]+)<", text)
        if juan_name:
            if juan_head != juan_name[0]:
                juan_head = juan_name[0]
            else:
                text = text.replace("'juan'", "'juan-end'")

        text = text.replace('><p', '>\n<p').split('\n')
        for j, t in enumerate(text):
            if len(re.findall('<p', t)) > 1:
                print('Line %d has multiple <p>' % (i + 1))
                return
            t = re.sub("<span class='lineInfo' line='[^']+'></span>", '', t.replace(' class=""', ''))
            if re.search('<p[> ]', t):
                pid += 1
                text[j] = re.sub("<p( id='[^']+')?", "<p id='p%d'" % pid, t)
            if re.search('lg-row', t):
                gid += 1
                text[j] = re.sub("class='lg-row'( id='[^']+')?", "class='lg-row' id='g%d'" % gid, t)
        lines[i] = '\n'.join(text)
    print('%d, %d ids added' % (pid, gid))
    with open(dst_file or src_file, 'w') as f:
        f.writelines(lines)


if __name__ == '__main__':
    import fire

    fire.Fire(main)
