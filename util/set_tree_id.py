#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@desc: 
@author: Zhang Yungui
@time: 2020/4/22
"""

import json

items = [
   {
      "children": [
         {
            "children": [
               {
                  "text": "123"
               },
               {
                  "text": "1212"
               }
            ],
            "text": "22"
         }
      ],
      "text": "2"
   },
   {
      "text": "222"
   }
]
nodes = []


def process(nodes, new_id):
    for node in nodes:
        node['id'] = new_id
        new_id += 1
    for node in nodes:
        if node.get('children'):
            new_id = process(node['children'], new_id)
    return new_id


process(items, 1)
with open('_tree.json', 'w') as f:
    json.dump(items, f, ensure_ascii=False)
