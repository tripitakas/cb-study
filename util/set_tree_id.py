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
        "text": "題",
        "id": 2
      },
      {
        "text": "歸敬述意",
        "children": [
          {
            "text": "偈頌",
            "children": [
              {
                "text": "歸憑三寶",
                "id": 27
              },
              {
                "text": "述造論意",
                "id": 28
              }
            ],
            "id": 10
          },
          {
            "text": "長文",
            "children": [
              {
                "text": "重述意",
                "id": 29
              },
              {
                "text": "正立科",
                "id": 30
              }
            ],
            "id": 11
          }
        ],
        "id": 3
      },
      {
        "text": "一、因缘分（作因）",
        "children": [
          {
            "text": "正明八因",
            "id": 12
          },
          {
            "text": "釋疑明意",
            "children": [
              {
                "text": "釋疑",
                "id": 31
              },
              {
                "text": "明意",
                "id": 32
              }
            ],
            "id": 13
          }
        ],
        "id": 4
      },
      {
        "text": "二、立義分",
        "children": [
          {
            "text": "初標",
            "id": 14
          },
          {
            "text": "法（[唐]有法）",
            "id": 15,
            "children": [
              {
                "text": "真如-体",
                "id": 33
              },
              {
                "text": "生灭-体相用",
                "id": 34
              }
            ]
          },
          {
            "text": "義（[唐]法）",
            "children": [
              {
                "text": "大(約法)",
                "id": 33
              },
              {
                "text": "乘(約喻)",
                "id": 34
              }
            ],
            "id": 16
          }
        ],
        "id": 5
      },
      {
        "text": "三、解釋分",
        "children": [
          {
            "text": "立科",
            "id": 17
          },
          {
            "text": "顯示實義",
            "children": [
              {
                "text": "總標二門",
                "id": 35
              },
              {
                "text": "心真如門",
                "children": [
                  {
                    "text": "心真如相",
                    "children": [
                      {
                        "text": "正詮法體",
                        "children": [
                          {
                            "text": "借言詮法",
                            "id": 102
                          },
                          {
                            "text": "顯法離言",
                            "id": 103
                          }
                        ],
                        "id": 79
                      },
                      {
                        "text": "隨順悟入",
                        "id": 80
                      }
                    ],
                    "id": 57
                  },
                  {
                    "text": "示大乘體",
                    "children": [
                      {
                        "text": "略標釋",
                        "id": 81
                      },
                      {
                        "text": "廣釋成",
                        "children": [
                          {
                            "text": "空義",
                            "id": 104
                          },
                          {
                            "text": "不空義",
                            "id": 105
                          }
                        ],
                        "id": 82
                      }
                    ],
                    "id": 58
                  }
                ],
                "id": 46
              },
              {
                "text": "心生滅門",
                "children": [
                  {
                    "text": "心生滅因緣相",
                    "children": [
                      {
                        "text": "明染淨生滅",
                        "children": [
                          {
                            "text": "正釋心生滅",
                            "children": [
                              {
                                "text": "標名列義",
                                "id": 132
                              },
                              {
                                "text": "依義各釋",
                                "children": [
                                  {
                                    "text": "覺義",
                                    "children": [
                                      {
                                        "text": "總立本始兩覺",
                                        "id": 170
                                      },
                                      {
                                        "text": "別辨本始兩覺",
                                        "children": [
                                          {
                                            "text": "辨始覺義",
                                            "children": [
                                              {
                                                "text": "總標淺深",
                                                "id": 198
                                              },
                                              {
                                                "text": "詳示淺深",
                                                "id": 199
                                              },
                                              {
                                                "text": "明淺深無性",
                                                "id": 200
                                              }
                                            ],
                                            "id": 190
                                          },
                                          {
                                            "text": "辨本覺義",
                                            "children": [
                                              {
                                                "text": "標二相",
                                                "id": 201
                                              },
                                              {
                                                "text": "釋二相",
                                                "children": [
                                                  {
                                                    "text": "淨智相",
                                                    "children": [
                                                      {
                                                        "text": "示相",
                                                        "id": 215
                                                      },
                                                      {
                                                        "text": "釋成",
                                                        "id": 216
                                                      }
                                                    ],
                                                    "id": 210
                                                  },
                                                  {
                                                    "text": "不思議用相",
                                                    "id": 211
                                                  }
                                                ],
                                                "id": 202
                                              }
                                            ],
                                            "id": 191
                                          }
                                        ],
                                        "id": 171
                                      },
                                      {
                                        "text": "總顯四種大義",
                                        "id": 172
                                      }
                                    ],
                                    "id": 158
                                  },
                                  {
                                    "text": "不覺義",
                                    "children": [
                                      {
                                        "text": "總明不覺依覺故無實",
                                        "id": 173
                                      },
                                      {
                                        "text": "別示不覺虛妄相",
                                        "id": 174
                                      }
                                    ],
                                    "id": 159
                                  }
                                ],
                                "id": 133
                              },
                              {
                                "text": "總辨同異",
                                "children": [
                                  {
                                    "text": "標",
                                    "id": 160
                                  },
                                  {
                                    "text": "釋",
                                    "children": [
                                      {
                                        "text": "同相",
                                        "id": 175
                                      },
                                      {
                                        "text": "異相",
                                        "id": 176
                                      }
                                    ],
                                    "id": 161
                                  }
                                ],
                                "id": 134
                              }
                            ],
                            "id": 106
                          },
                          {
                            "text": "明生滅因緣",
                            "children": [
                              {
                                "text": "明迷染因緣",
                                "children": [
                                  {
                                    "text": "總明依心故轉",
                                    "id": 162
                                  },
                                  {
                                    "text": "別釋意及意識",
                                    "children": [
                                      {
                                        "text": "意",
                                        "id": 177
                                      },
                                      {
                                        "text": "意識",
                                        "id": 178
                                      }
                                    ],
                                    "id": 163
                                  }
                                ],
                                "id": 135
                              },
                              {
                                "text": "明悟淨因緣",
                                "children": [
                                  {
                                    "text": "總明悟有淺深",
                                    "id": 164
                                  },
                                  {
                                    "text": "詳釋淺深差別",
                                    "children": [
                                      {
                                        "text": "總明義深",
                                        "id": 179
                                      },
                                      {
                                        "text": "別示次第",
                                        "children": [
                                          {
                                            "text": "正釋悟淨次第",
                                            "children": [
                                              {
                                                "text": "離染心次第",
                                                "id": 203
                                              },
                                              {
                                                "text": "離不覺次第",
                                                "id": 204
                                              }
                                            ],
                                            "id": 192
                                          },
                                          {
                                            "text": "轉釋相應不相應義",
                                            "id": 193
                                          }
                                        ],
                                        "id": 180
                                      },
                                      {
                                        "text": "結示二障",
                                        "id": 181
                                      }
                                    ],
                                    "id": 165
                                  }
                                ],
                                "id": 136
                              }
                            ],
                            "id": 107
                          },
                          {
                            "text": "辨生滅之相",
                            "children": [
                              {
                                "text": "正分別",
                                "id": 137
                              },
                              {
                                "text": "問答釋疑",
                                "id": 138
                              }
                            ],
                            "id": 108
                          }
                        ],
                        "id": 83
                      },
                      {
                        "text": "明染淨熏習",
                        "children": [
                          {
                            "text": "總標熏習義",
                            "id": 109
                          },
                          {
                            "text": "熏習染法",
                            "children": [
                              {
                                "text": "正明熏義",
                                "id": 139
                              },
                              {
                                "text": "釋義差別",
                                "id": 140
                              }
                            ],
                            "id": 110
                          },
                          {
                            "text": "熏習淨法",
                            "children": [
                              {
                                "text": "正明熏義",
                                "id": 141
                              },
                              {
                                "text": "釋義差別",
                                "children": [
                                  {
                                    "text": "妄熏義別",
                                    "id": 166
                                  },
                                  {
                                    "text": "真熏義別",
                                    "children": [
                                      {
                                        "text": "標",
                                        "id": 182
                                      },
                                      {
                                        "text": "釋",
                                        "children": [
                                          {
                                            "text": "體熏",
                                            "children": [
                                              {
                                                "text": "正釋",
                                                "id": 205
                                              },
                                              {
                                                "text": "釋疑",
                                                "children": [
                                                  {
                                                    "text": "疑問",
                                                    "id": 212
                                                  },
                                                  {
                                                    "text": "約無明煩惱厚薄釋",
                                                    "id": 213
                                                  },
                                                  {
                                                    "text": "約因緣互相成辦釋",
                                                    "id": 214
                                                  }
                                                ],
                                                "id": 206
                                              }
                                            ],
                                            "id": 194
                                          },
                                          {
                                            "text": "用熏",
                                            "children": [
                                              {
                                                "text": "略標",
                                                "id": 207
                                              },
                                              {
                                                "text": "差別緣",
                                                "id": 208
                                              },
                                              {
                                                "text": "平等緣",
                                                "id": 209
                                              }
                                            ],
                                            "id": 195
                                          }
                                        ],
                                        "id": 183
                                      },
                                      {
                                        "text": "結判",
                                        "id": 184
                                      }
                                    ],
                                    "id": 167
                                  }
                                ],
                                "id": 142
                              }
                            ],
                            "id": 111
                          },
                          {
                            "text": "結判斷與不斷",
                            "id": 112
                          }
                        ],
                        "id": 84
                      }
                    ],
                    "id": 59
                  },
                  {
                    "text": "顯示大乘體相用",
                    "children": [
                      {
                        "text": "顯示體相",
                        "children": [
                          {
                            "text": "正顯示",
                            "id": 113
                          },
                          {
                            "text": "釋疑",
                            "id": 114
                          }
                        ],
                        "id": 85
                      },
                      {
                        "text": "顯示用",
                        "children": [
                          {
                            "text": "正明用即真如",
                            "id": 115
                          },
                          {
                            "text": "廣明隨機見別",
                            "children": [
                              {
                                "text": "約所依識以判二身",
                                "id": 143
                              },
                              {
                                "text": "約機所見以判粗細",
                                "id": 144
                              }
                            ],
                            "id": 116
                          },
                          {
                            "text": "結示真如妙用",
                            "id": 117
                          }
                        ],
                        "id": 86
                      }
                    ],
                    "id": 60
                  }
                ],
                "id": 47
              },
              {
                "text": "真生不二（不離）",
                "children": [
                  {
                    "text": "正示觀門",
                    "children": [
                      {
                        "text": "標意",
                        "id": 61
                      },
                      {
                        "text": "明觀",
                        "id": 62
                      }
                    ],
                    "id": 48
                  },
                  {
                    "text": "喻顯不二",
                    "id": 49
                  }
                ],
                "id": 37
              }
            ],
            "id": 18
          },
          {
            "text": "對治邪執",
            "children": [
              {
                "text": "總標二見",
                "id": 38
              },
              {
                "text": "別釋二見",
                "children": [
                  {
                    "text": "人我見",
                    "children": [
                      {
                        "text": "正除我見",
                        "id": 63
                      },
                      {
                        "text": "例破餘見",
                        "id": 64
                      }
                    ],
                    "id": 50
                  },
                  {
                    "text": "法我見",
                    "children": [
                      {
                        "text": "起執之由",
                        "id": 65
                      },
                      {
                        "text": "對治之法",
                        "children": [
                          {
                            "text": "正明",
                            "id": 87
                          },
                          {
                            "text": "釋疑",
                            "id": 88
                          }
                        ],
                        "id": 66
                      }
                    ],
                    "id": 51
                  }
                ],
                "id": 39
              }
            ],
            "id": 19
          },
          {
            "text": "分別修行正道相",
            "children": [
              {
                "text": "總標",
                "id": 40
              },
              {
                "text": "各釋",
                "children": [
                  {
                    "text": "信成就發心",
                    "children": [
                      {
                        "text": "征起",
                        "id": 67
                      },
                      {
                        "text": "解釋",
                        "children": [
                          {
                            "text": "信成就",
                            "children": [
                              {
                                "text": "正釋成就",
                                "id": 118
                              },
                              {
                                "text": "兼釋未成",
                                "id": 119
                              }
                            ],
                            "id": 89
                          },
                          {
                            "text": "發心",
                            "children": [
                              {
                                "text": "所發之心",
                                "id": 120
                              },
                              {
                                "text": "發心之行",
                                "id": 121
                              },
                              {
                                "text": "發心之益",
                                "children": [
                                  {
                                    "text": "約實明能",
                                    "id": 145
                                  },
                                  {
                                    "text": "約權簡過",
                                    "id": 146
                                  },
                                  {
                                    "text": "以實破權",
                                    "id": 147
                                  }
                                ],
                                "id": 122
                              }
                            ],
                            "id": 90
                          }
                        ],
                        "id": 68
                      }
                    ],
                    "id": 52
                  },
                  {
                    "text": "解行發心",
                    "children": [
                      {
                        "text": "明位",
                        "id": 69
                      },
                      {
                        "text": "明行",
                        "id": 70
                      }
                    ],
                    "id": 53
                  },
                  {
                    "text": "證發心",
                    "children": [
                      {
                        "text": "分證",
                        "children": [
                          {
                            "text": "明所證",
                            "children": [
                              {
                                "text": "證體",
                                "id": 123
                              },
                              {
                                "text": "起用",
                                "id": 124
                              }
                            ],
                            "id": 91
                          },
                          {
                            "text": "明心相",
                            "id": 92
                          }
                        ],
                        "id": 71
                      },
                      {
                        "text": "滿證",
                        "children": [
                          {
                            "text": "依權示相",
                            "id": 93
                          },
                          {
                            "text": "依實釋疑",
                            "children": [
                              {
                                "text": "釋一切種智疑",
                                "id": 125
                              },
                              {
                                "text": "釋任運利生疑",
                                "id": 126
                              }
                            ],
                            "id": 94
                          }
                        ],
                        "id": 72
                      }
                    ],
                    "id": 54
                  }
                ],
                "id": 41
              }
            ],
            "id": 20
          }
        ],
        "id": 6
      },
      {
        "text": "四、修信分",
        "children": [
          {
            "text": "正明修習信心",
            "children": [
              {
                "text": "徵",
                "id": 42
              },
              {
                "text": "釋",
                "children": [
                  {
                    "text": "信心",
                    "id": 55
                  },
                  {
                    "text": "修習",
                    "children": [
                      {
                        "text": "總標",
                        "id": 73
                      },
                      {
                        "text": "施門",
                        "id": 74
                      },
                      {
                        "text": "戒門",
                        "id": 75
                      },
                      {
                        "text": "忍門",
                        "id": 76
                      },
                      {
                        "text": "精進門",
                        "children": [
                          {
                            "text": "總明精進意",
                            "id": 95
                          },
                          {
                            "text": "別示精進法",
                            "id": 96
                          }
                        ],
                        "id": 77
                      },
                      {
                        "text": "止觀門",
                        "children": [
                          {
                            "text": "總標",
                            "id": 97
                          },
                          {
                            "text": "釋止",
                            "children": [
                              {
                                "text": "明修相",
                                "children": [
                                  {
                                    "text": "方便",
                                    "id": 148
                                  },
                                  {
                                    "text": "正修",
                                    "id": 149
                                  },
                                  {
                                    "text": "揀成不成",
                                    "id": 150
                                  }
                                ],
                                "id": 127
                              },
                              {
                                "text": "明證相",
                                "children": [
                                  {
                                    "text": "正明證相",
                                    "id": 151
                                  },
                                  {
                                    "text": "辨析魔事",
                                    "children": [
                                      {
                                        "text": "示魔事相",
                                        "children": [
                                          {
                                            "text": "致魔之由",
                                            "id": 185
                                          },
                                          {
                                            "text": "魔事之相",
                                            "children": [
                                              {
                                                "text": "辨形聲",
                                                "id": 196
                                              },
                                              {
                                                "text": "辨起過",
                                                "id": 197
                                              }
                                            ],
                                            "id": 186
                                          },
                                          {
                                            "text": "魔亂之失",
                                            "id": 187
                                          }
                                        ],
                                        "id": 168
                                      },
                                      {
                                        "text": "示對治法",
                                        "children": [
                                          {
                                            "text": "治邪",
                                            "id": 188
                                          },
                                          {
                                            "text": "歸正",
                                            "id": 189
                                          }
                                        ],
                                        "id": 169
                                      }
                                    ],
                                    "id": 152
                                  }
                                ],
                                "id": 128
                              },
                              {
                                "text": "勸修",
                                "children": [
                                  {
                                    "text": "正勸",
                                    "id": 153
                                  },
                                  {
                                    "text": "明益",
                                    "id": 154
                                  }
                                ],
                                "id": 129
                              }
                            ],
                            "id": 98
                          },
                          {
                            "text": "釋觀",
                            "children": [
                              {
                                "text": "明應修",
                                "id": 130
                              },
                              {
                                "text": "明修相",
                                "children": [
                                  {
                                    "text": "四諦觀",
                                    "id": 155
                                  },
                                  {
                                    "text": "弘願觀",
                                    "id": 156
                                  },
                                  {
                                    "text": "起行觀",
                                    "id": 157
                                  }
                                ],
                                "id": 131
                              }
                            ],
                            "id": 99
                          },
                          {
                            "text": "雙行",
                            "id": 100
                          },
                          {
                            "text": "結益",
                            "id": 101
                          }
                        ],
                        "id": 78
                      }
                    ],
                    "id": 56
                  }
                ],
                "id": 43
              }
            ],
            "id": 21
          },
          {
            "text": "更示勝異方便",
            "children": [
              {
                "text": "泛明念佛除障",
                "id": 44
              },
              {
                "text": "的指求生極樂",
                "id": 45
              }
            ],
            "id": 22
          }
        ],
        "id": 7
      },
      {
        "text": "五、利益分",
        "children": [
          {
            "text": "總勸聞思修",
            "id": 23
          },
          {
            "text": "別示聞思修功德",
            "id": 24
          },
          {
            "text": "誡誹謗獲大罪",
            "id": 25
          },
          {
            "text": "結示大乘功能",
            "id": 26
          }
        ],
        "id": 8
      },
      {
        "text": "結施迴向",
        "id": 9
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
