// 根据注解锚点插入注解段落
function insertNotes($side, notes, opt) {
  opt = opt || {};
  $side.find('.note-tag').each(function() {
    let $tag = $(this),
        id = parseInt($tag.attr('data-note-id')),
        note = notes.filter(item => item[0] == id)[0],
        $kePan = $tag.closest('[kepan]'),
        title = [], rows = [];

    if (opt['tag'] && $tag.text().indexOf(opt['tag']) < 0) {
      return;
    }
    console.assert(note && note.length % 3 === 0, id + ' mismatch');
    for (let i = 0; i + 2 < note.length; i += 3) {
      title.push(note[i + 1]);
      rows.push('<span class="note-item"><span class="org-text">' +
        (note[i + 1].length > 4 ? note[i + 1].substring(0, 3) +
            '<span class="more" data-more="' + note[i + 1].substring(3) + '">…</span>' : note[i + 1]) +
        '</span><span class="note-text">' + note[i + 2] + '</span></span>');
    }
    if (rows.length > 1 && opt['showMergedNotes']) {
      console.log(rows);
      $tag.text($tag.text() + rows.length);
      setTimeout(() => $tag.click() );
    }
    if (!$kePan[0]) {
      $kePan = $tag.parent();
    }
    $tag.attr('title', (opt['name'] ? '《' + opt['name'] + '》: ' : '') + title.join('\n'));

    if (opt['showAnchorPostfix']) {
      let s = title.join('|');
      if (s.length > 20) {
        s = s.substring(0, 8) + '…<b style="color:#333;">' + s.substring(s.length - 8) + '</b>';
      }
      $tag.html($tag.text() + s);
    }

    $('<p class="note-p" data-note-id="' + id + '">' + rows.join('<br>') + '</p>')
      .insertAfter($kePan.closest('.lg').length ? $kePan.closest('.lg') : $kePan);
  });
}

// 单击注解锚点标记则展开注解段落
$(document).on('click', '.note-tag', function (e) {
  let $this = $(e.target),
      id = $this.attr('data-note-id'),
      $p = $this.closest('.cell-l, .cell-r').find('.note-p[data-note-id=' + id + ']');

  $p.toggle();
  $this.toggleClass('note-expanded');
  e.stopPropagation();
});

// 双击注解段落则收起隐藏
$(document).on('dblclick', '.note-p', function (e) {
  let $p = $(e.target).closest('.note-p'),
      id = $p.attr('data-note-id'),
      $tag = $p.closest('.cell-l, .cell-r').find('.note-tag[data-note-id=' + id + ']');
  $p.toggle();
  $tag.toggleClass('note-expanded');
  e.stopPropagation();
});

// 单击 … 展开文字
$(document).on('click', '.more', function (e) {
  let $s = $(e.target);
  $s.text($s.text() === '…' ? $s.attr('data-more') : '…');
});

// 显隐全部注解
$('#show-notes').click(() => {
  let expanded = $('.note-tag.note-expanded').length;
  $('.note-p').toggle(!expanded);
  $('.note-tag').toggleClass('note-expanded', !expanded);
});

// 单击注释切换当前条
$(document).on('click', '.note-text', function (e) {
  $(e.target).closest('.cell-l, .cell-r').find('.note-item').removeClass('active');
  $(e.target).closest('.note-item').addClass('active');
});
