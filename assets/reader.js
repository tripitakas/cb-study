$('#show-line-no').click(() => {
  $('p').each((i, p) => {
    const $p = $(p);
    if ($p.find('.line-no').length) {
      $p.find('.line-no').remove();
    } else {
      $p.prepend($('<span class="line-no">[' + $p.attr('id').substring(1) + ']</span>'));
    }
  });
  $('.lg').each((i, p) => {
    const $p = $(p);
    if ($p.find('.line-no').length) {
      $p.find('.line-no').remove();
    } else {
      $p.prepend($('<span class="line-no">[' + $p.attr('id') + ']</span>'));
    }
  });
});

$('#show-xu').click(() => {
  $('.div-xu').toggle();
});

$('#show-box').click(() => {
  $('#merged').toggleClass('show-box');
});

var fontSize = 14;

$('#enlarge-font').click(() => {
  if (fontSize < 36) {
    fontSize++;
    $('body').css('font-size', fontSize + 'px');
  }
});

$('#reduce-font').click(() => {
  if (fontSize > 8) {
    fontSize--;
    $('body').css('font-size', fontSize + 'px');
  }
});

function toSelId(s) {
  if (s) {
    if (s[0] !== '.' && s[0] !== '#') {
      if (/^\d/.test(s)) {
        s = 'p' + s;
      }
      s = '#' + s;
    }
  }
  return s;
}

function movePairs(ids) {
  const ids1 = (ids.split('|')[0] || '').split(' ').map(toSelId).filter(function (s) { return s; });
  const ids2 = (ids.split('|')[1] || '').split(' ').map(toSelId).filter(function (s) { return s; });
  const $row = $('<div class="row"><div class="col-xs-6 cell-l"/><div class="col-xs-6 cell-r"/></div>');
  const $left = $row.find('.cell-l'), $right = $row.find('.cell-r');

  if (!ids1.length && !ids2.length) {
    return;
  }
  for (let id of ids1) {
    let el = $article1.find(id);
    if (el.length) {
      el.remove();
      $left.append(el);
    }
  }
  for (let id of ids2) {
    let el = $article2.find(id);
    console.assert(el.length, id + ' not found: ' + ids);
    if (el.length) {
      el.remove();
      $right.append(el);
    }
  }
  $('#merged').append($row);
}