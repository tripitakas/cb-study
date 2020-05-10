#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@desc: 比较多个文本文件，输出比较结果网页
@time: 2020/5/8
"""
import re
import subprocess
from os import path
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tool.diff import Diff

data = {}


class MainHandler(RequestHandler):
    def get(self):
        def is_empty(t):
            return not t or re.match(r'^[\s\n\u3000]*$', t)

        def is_punctuation(t):
            return re.match(r'^[，、：；。？！][\s\n]*$', t or '')

        def add_segment():
            if not segments or segments[-1][0] != s['line_no']:
                segments.append((s['line_no'], []))
            segments[-1][1].append(s)

            items.append(s)
            if s['is_same'] and data.get('remove_dup'):
                if len(s['base']) > 12:
                    t = list(s['base'])
                    t[6:-6] = ['…']
                    s['base'] = ''.join(t)
                if len(items) > 2 and items[-2]['is_same'] and items[-3]['is_same']:
                    items[-2]['base'] = ''

        items = []
        segments = []
        pre_empty_line_no = 0
        for s in data['diff_segments']:
            s = dict(s)
            base = s.get('base', '').strip()
            cmp1 = s.get('cmp1', '').strip()
            if is_empty(base) and is_empty(cmp1) and is_empty(s.get('cmp2')):
                s['is_same'] = True
                s['base'] = '\n'
            elif is_punctuation(base) and (is_empty(cmp1) or cmp1 == '。'):
                s['is_same'] = True
            if s['is_same'] and s['base'] == '\n':  # 当前为空行，即换行
                if not pre_empty_line_no:  # 连续空行仅保留第一个
                    add_segment()
                pre_empty_line_no += 1
            else:  # 当前非空行
                add_segment()
                pre_empty_line_no = 0

        html = self.render_string('index.html', segments=segments, **data)
        with open('data/result_%s.html' % data['title'], 'wb') as f:
            f.write(html)
        self.render('index.html', segments=segments, **data)


def read_txt(src_file, overwrite):
    if src_file.endswith('.html') and 0:
        with open(src_file) as f:
            text = f.read()
        with open(src_file + '-', 'w') as f:
            f.write(re.sub(r"(<span class='doube-line-note'>)([^(][^<]*)(</span)",
                           lambda m: '%s(%s)%s' % (m.group(1), m.group(2), m.group(3)), text))
    if not src_file.endswith('.txt'):
        txt_file = path.splitext(src_file)[0] + '.txt'
        if overwrite or not path.exists(txt_file):
            office = '/Applications/LibreOffice.app/Contents/MacOS/soffice'
            subprocess.call([office, '--headless', '--convert-to', 'txt', '--norestore',
                             '--outdir', path.dirname(src_file), src_file])
        src_file = txt_file
    text = open(src_file).read()
    text = text.replace('(', '（').replace(')', '）')
    text = re.sub('[①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚㉛㉜㉝㉞㉟㊱㊲㊳㊴㊵㊶㊷㊸㊹㊺㊻㊼㊽㊾㊿0-9]', '', text)
    text = re.sub(r'（[甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥]）', '', text)
    text = re.sub(r'[“”‘’「」『』〈〉《》（）]', '', text)
    # text = re.sub(r'[，、：；。？！]', '', text)
    text = re.sub(r'\n[\t ]+|\n+', r'\n', text, re.M)
    text = re.sub(r'(科判索引|【經文資訊】)(.|\n)+$', '', text, re.M)
    return text


def main(title, base_file, second_file, *more_files, label=None, overwrite=False, remove_dup=True, port=8888):
    files = [base_file, second_file] + list(more_files)
    label = label and label.split(',') or ['base', 'cmp1'] + ['cmp%d' % (i + 2) for i in range(len(more_files))]
    assert not label or len(label) == len(files), 'mismatch label'
    data['label'] = {'cmp%d' % i if i else 'base': t for i, t in enumerate(label)}
    data['contents'] = ct = {i: read_txt(f, overwrite) for i, f in enumerate(files)}
    data['diff_segments'] = Diff.diff(ct[0], ct[1], ct.get(2), ct.get(3))[0]
    data['title'] = title
    data['remove_dup'] = remove_dup

    app = Application([
        ('/', MainHandler),
    ], static_path='static', compiled_template_cache=False)
    app.listen(port)
    print('http://localhost:%d' % port)
    try:
        IOLoop.current().start()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main('裂網疏', 'data/裂網疏.docx', 'data/T1850.html', label='慕,CB')
    # import fire
    # fire.Fire(main)
