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

$('#show-hide-txt').click(() => {
  $('#merged').toggleClass('show-hide-txt');
});

$('#show-left').click(() => {
  let $left = $('#merged .cell-l'), $right = $('#merged .cell-r');
  $left.removeClass('col-xs-6');
  $left.show();
  $right.hide();
});

$('#show-right').click(() => {
  let $left = $('#merged .cell-l'), $right = $('#merged .cell-r');
  $right.removeClass('col-xs-6');
  $right.show();
  $left.hide();
});

$('#show-both').click(() => {
  let $left = $('#merged .cell-l'), $right = $('#merged .cell-r');
  $left.addClass('col-xs-6');
  $right.addClass('col-xs-6');
  $left.show();
  $right.show();
});


let fontSize = 16;

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
  const $article1 = $('.original#body-left'),
      $article2 = $('.original#body-right'),
      ids1 = (ids.split('|')[0] || '').split(' ').map(toSelId).filter(function (s) { return s; }),
      ids2 = (ids.split('|')[1] || '').split(' ').map(toSelId).filter(function (s) { return s; }),
      $row = $('<div class="row"><div class="col-xs-6 cell-l"/><div class="col-xs-6 cell-r"/></div>'),
      $left = $row.find('.cell-l'), $right = $row.find('.cell-r');
  let count = 0;

  if (!ids1.length && !ids2.length) {
    return;
  }
  for (let id of ids1) {
    let id2 = id.replace(/-$/, ''), el = $article1.find(id2);
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
