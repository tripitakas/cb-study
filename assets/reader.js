// 显隐行号
$('#show-line-no').click(() => {
  $('p, .lg').each((i, p) => {
    const $p = $(p);
    if ($p.find('.line-no').length) {
      $p.find('.line-no').remove();
    } else {
      $p.prepend($('<span class="line-no">[' + $p.attr('id').replace(/^p/, '') + ']</span>'));
    }
  });
});

// 显隐序言
$('#show-xu').click(() => {
  $('.div-xu').toggle();
});

// 显隐段落和span框，用于调试科判分布
$('#show-box').click(() => {
  $('body').toggleClass('show-box');
});

$('#show-hide-txt').click(() => {
  $('body').toggleClass('show-hide-txt');
});

// 显示左边文
$('#show-left').click(() => {
  let $left = $('.cell-l'), $right = $('.cell-r');
  $left.removeClass('col-xs-6');
  $left.show();
  $right.hide();
  $left.parent().parent().addClass('single-article');
});

// 显示右边文
$('#show-right').click(() => {
  let $left = $('.cell-l'), $right = $('.cell-r');
  $right.removeClass('col-xs-6');
  $right.show();
  $left.hide();
  $left.parent().parent().addClass('single-article');
});

// 显示左右对照文
$('#show-both').click(() => {
  let $left = $('.cell-l'), $right = $('.cell-r');
  $left.addClass('col-xs-6');
  $right.addClass('col-xs-6');
  $left.show();
  $right.show();
  $left.parent().parent().removeClass('single-article');
});

// 正文增大字号
$('#enlarge-font').click(() => {
  let fontSize = parseInt($('#content').css('font-size'));
  if (fontSize < 36) {
    fontSize++;
    $('#content, #merged').css('font-size', fontSize + 'px');
  }
});

// 正文减小字号
$('#reduce-font').click(() => {
  let fontSize = parseInt($('#content').css('font-size'));
  if (fontSize > 8) {
    fontSize--;
    $('#content, #merged').css('font-size', fontSize + 'px');
  }
});

// 将多个段落编号的串转换为选择器数组
function toPairSelectors(idsText) {
  return idsText.split(' ').filter(s => s).map(s => {
    if (s[0] !== '.' && s[0] !== '#') {
      if (/^\d/.test(s)) {
        s = 'p' + s;
      }
      s = '#' + s;
    }
    return s;
  });
}

// 将一行编号（格式为“ id id... | id...”）的段落元素移到#merged的左右对照元素内
function movePairs(ids) {
  const $article1 = $('.original#body-left'),
      $article2 = $('.original#body-right'),
      ids1 = toPairSelectors(ids.split('|')[0] || ''),
      ids2 = toPairSelectors(ids.split('|')[1] || ''),
      $row = $('<div class="row"><div class="col-xs-6 cell-l"/><div class="col-xs-6 cell-r"/></div>'),
      $left = $row.find('.cell-l'), $right = $row.find('.cell-r');
  let count = 0;

  if (!ids1.length && !ids2.length) {
    return;
  }
  for (let id of ids1) {
    let id2 = id.replace(/-$/, ''), el = $article1.find(id2); // 编号末尾有减号表示转为隐藏文本
    console.assert(el.length, id2 + ' not found: ' + ids);
    if (el.length) {
      el.remove();
      if (/-$/.test(id)) {
        el.addClass('hide-txt');
      } else {
        count++;
      }
      $left.append(el);
    }
  }
  for (let id of ids2) {
    let id2 = id.replace(/-$/, ''), el = $article2.find(id2);
    console.assert(el.length, id2 + ' not found: ' + ids);
    if (el.length) {
      el.remove();
      if (/-$/.test(id)) {
        el.addClass('hide-txt');
      } else {
        count++;
      }
      $right.append(el);
    }
  }
  if (count === 0) {
    $row.addClass('hide-txt');
  }
  $('#merged').append($row);
}

// 单击科判节点后将当前选中文本提取为一个span，并设置其科判编号
function convertToSpanWithTag(tag, value, text) {
  let sel = window.getSelection(),  // 选中范围，非IE
      node = sel.anchorNode,  // 选择区的起点对象，要与结束对象focusNode相同，且为P内不属于span的普通文字
      p = node && node.parentElement, // 段落元素，应为P
      selText = sel.toString(); // 选择的文字

  if (selText && value && text && p && p.tagName === 'P' && node === sel.focusNode && node.nodeName === '#text') {
    p.innerHTML = p.innerHTML.replace(selText, '<span ' + tag + '="' + value +'">' + selText +
        '<sup>[' + value + ':' + text.substring(0, 4) + ']</sup></span>');
  } else {
    console.log(value, text, p);
  }
}

// 切换显隐正文内的科判标记，段内各项分行显示
function showInlineJudgments() {
  const tree = $.jstree.reference('#judgments');

  $('body').toggleClass('show-inline-kepan');
  $('body').removeClass('hide-kepan-txt');
  $('span[kepan]').each((i, s) => {
    let $s = $(s), $j = $s.find('.kepan-text');

    if ($j.length) {
      $j.remove();
    } else {
      const node = tree.get_node($s.attr('kepan'));
      if (node) {
        $j = $('<span class="kepan-text">[' + node.text.replace(/^.+、|[(（].+$/g, '') + ']</span>');
        $s.append($j);
      }
    }
  });
}

// 切换显隐正文内的科判标记，段内各项分行显示
$('#show-inline-kepan').click(showInlineJudgments);

// 段内各项分行显示，不显示科判标记
$('#show-inline-no-kepan').click(() => {
  showInlineJudgments();
  $('body').addClass('hide-kepan-txt');
});

// 高亮显示科判节点对应的正文span片段
function highlightJudg(judgId, scroll, level) {
  const tree = $.jstree.reference('#judgments');
  let $s = $('[kepan="' + judgId + '"], [kepan^="' + judgId + 'p"]');

  $s.addClass('highlight');
  if ($s[0]) {
    setTimeout(() => {
      $s.removeClass('highlight');
    }, 1000);
  }

  if (!level) {
    $('[kepan]').removeClass('active');
    $('[kepan]').removeClass('hover');
  }
  $s.addClass('active');

  const nodes = tree.get_children_dom(judgId);
  if (nodes) {
    for (let node of nodes.get()) {
      let r = highlightJudg(node.getAttribute('id'), false, (level || 0) + 1);
      $s = $s[0] ? $s : r;
    }
  }

  if (scroll && scroll !== 'click' && $s[0]) {
    const box = $s[0].getBoundingClientRect();
    let st = document.body.scrollTop, h = document.body.clientHeight;

    if (box.y < 100 || box.y + box.height + 200 > h) {
      st += box.y < 100 ? box.y - 100 : box.y + box.height + 200 - h;
      $('html,body').animate({scrollTop: st}, 500);
    }
  }
  if (scroll && scroll !== 'nav') {
    if (scroll !== 2) {  // footer
      showJudgPath(judgId);
    }
    tree.deselect_all(true);
    tree.select_node(judgId, true);
  }

  return $s;
}

// 在状态栏显示科判路径
function showJudgPath(judgId) {
  const tree = $.jstree.reference('#judgments');
  const node = tree.get_node(judgId);
  let texts = [];

  if (node) {
    for (let p of node.parents) {
      let t = tree.get_node(p).text;
      if (t) {
        texts.splice(0, 0, '<a onclick="highlightJudg(' + p + ',2)">' + t + '</a>');
      }
    }
    texts.push('<a onclick="highlightJudg(' + judgId + ',2)">' + node.text + '</a>');
  }

  $('.kepan-path').html(texts.join(' / '));
}

function getJudgId(el) {
  for (let i = 0; i < 3 && el; i++, el = el.parentElement) {
    if (el.getAttribute('kepan')) {
      return parseInt(el.getAttribute('kepan'));
    }
  }
}

// 在正文有科判标记的span上鼠标掠过
$(document).on('mouseover', '[kepan]', function (e) {
  let judgId = getJudgId(e.target),
      tree = $.jstree.reference('#judgments'),
      node = tree.get_node(judgId),
      sel = 'span[kepan="' + judgId + '"]',
      spans = $(sel),
      row = $(e.target).closest('.row');

  $('.hover').removeClass('hover');
  if (spans.length % 2 === 0 && node && tree.get_children_dom(node).length < 1) {
    let leftSpans = row.find('.cell-l').find(sel),
        rightSpans = row.find('.cell-r').find(sel);
    if (leftSpans.length === rightSpans.length) {
      let leftIndex = leftSpans.get().indexOf(e.target),
          rightIndex = rightSpans.get().indexOf(e.target);
      if (leftIndex >= 0) {
        $(rightSpans[leftIndex]).addClass('hover');
        $(leftSpans[leftIndex]).addClass('hover');
      }
      else if (rightIndex >= 0) {
        $(leftSpans[rightIndex]).addClass('hover');
        $(rightSpans[rightIndex]).addClass('hover');
      }
    }
  }
});

// 在正文有科判标记的span上鼠标滑入
$(document).on('mouseenter', '[kepan]', function (e) {
  showJudgPath(getJudgId(e.target));
});

// 在正文有科判标记的span上鼠标滑出
$(document).on('mouseleave', '[kepan]', function (e) {
  let judgId = $('[kepan].active').attr('kepan');
  if (judgId) {
    showJudgPath(judgId);
  }
});

// 在正文有科判标记的span上点击
$(document).on('click', '[kepan]', function (e) {
  highlightJudg(getJudgId(e.target), 'click');
});


// 科判导航栏的宽度比例
$('.kepan-ratio a').on('click',function () {
  let ratio = $(this).text();
  if (parseInt(ratio) > 0) {
    $('body').removeClass('hide-left-bar');
    $('.left-nav').css('width', ratio);
    $('#content').css('padding-left', ratio);
  } else {
    $('body').addClass('hide-left-bar');
    $('#content').css('padding-left', 0);
  }
});

// 增加科判树的字号
$('#enlarge-kepan-font').click(() => {
  let $j = $('#judgments'), fontSize = parseInt($j.css('font-size'));
  if (fontSize < 24) {
    fontSize += 2;
    $j.css('font-size', fontSize + 'px');
  }
});

// 减小科判树的字号
$('#reduce-kepan-font').click(() => {
  let $j = $('#judgments'), fontSize = parseInt($j.css('font-size'));
  if (fontSize > 10) {
    fontSize -= 2;
    $j.css('font-size', fontSize + 'px');
  }
});

$.fn.changeElementType = function(newType) {
  let newElements = [];
  $(this).each(function() {
    let attrs = {};
    $.each(this.attributes, function(idx, attr) {
      attrs[attr.nodeName] = attr.nodeValue;
    });
    let newElement = $("<" + newType + "/>", attrs).append($(this).contents());
    $(this).replaceWith(newElement);
    newElements.push(newElement);
  });
  return $(newElements);
};

$('#to-table').click(() => {
  if ($('#content table').length) {
    return;
  }
  $('#content').append($('<table><tbody></tbody></table>'));
  let $table = $('#content table'), $rows = $('#content > .row');
  $rows.find('span[kepan]').each((i, el) => {
    $(el).changeElementType('P');
  });
  $rows.each((i, el) => {
    let $tr = $('<tr><td class="cell-l" width="50%"></td><td class="cell-r" width="50%"></td></tr>')
    $tr.find('.cell-l').append($($(el).find('.cell-l').html()));
    $tr.find('.cell-r').append($($(el).find('.cell-r').html()));
    $table.append($tr);
    $(el).remove();
  });
});
