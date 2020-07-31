function initGroupRows() {
  showLineNo();
  showParaBox();
  window.rowPairs = window.rowPairs || '';
  rowPairs.split('||').forEach(movePairs);
  showRowPairs();
}

function showRowPairs() {
  let s = rowPairs.replace(/\|{2}[\n\s\\]*/g, '||\\\n      ');
  $('.label-panel textarea').text(s.replace(/\\[\n\s\\]*$/, ''));
}

// 将多个段落编号的串转换为选择器数组
function _toPairSelectors(idsText) {
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
      ids1 = _toPairSelectors(ids.split('|')[0] || ''),
      ids2 = _toPairSelectors(ids.split('|')[1] || ''),
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

// 在原始段落上单击，切换是否属于当前组
$('#content p, #content .lg-row').click(function () {
  let $this = $(this),
      id = $this.attr('id'),
      inLeft = $this.closest('#body-left').length > 0,
      $curIds = $('.current-row .row-' + (inLeft ? 'left' : 'right') + '-ids');

  $this.toggleClass('in-cur-row');  // 切换亮显
  if ($curIds.find('#cur-' + id).length) {
    $curIds.find('#cur-' + id).remove();
  } else {
    $curIds.append($('<span id="cur-' + id + '">' + id + '</span>'));
  }
});

// 将当前组的段落移到上面的合并区
$('#move-row').click(function () {
  let $left = $('.current-row .row-left-ids'),
      $right = $('.current-row .row-right-ids'),
      leftIds = $left.find('span').map((i, s) => $(s).text()).get().join(' '),
      rightIds = $right.find('span').map((i, s) => $(s).text()).get().join(' ');

  $('.in-cur-row').removeClass('in-cur-row');
  $left.html('');
  $right.html('');

  if (leftIds || rightIds) {
    movePairs(leftIds + ' | ' + rightIds);
    rowPairs += leftIds + ' | ' + rightIds + ' ||';
    showRowPairs();
  }
});