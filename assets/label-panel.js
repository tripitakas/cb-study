let $labelPanel = $('.label-panel > div'),
    $content = $('.cell-r'),
    notes = T1850Notes, noteTag = '[裂]';

notes.forEach(note => {
  let $tag = $content.find('[kepan] > [data-note-id=' + note[0] + ']');
  $labelPanel.append($('<p id="note' + note[0] + '" class="' + ($tag.length ? 'linked' : '') +
    '">' + note[0] + ': <span>' + note[1] + '</span>: ' + note[2] + '</p>'));
});

$labelPanel.dblclick(function() {
  $('.label-panel p:first-child').remove();
});

$(document).on('click', '.label-panel p>span', function (e) {
  let $p = $(e.target).closest('p'),
      id = $p.attr('id').substring(4),
      $tag = $content.find('.note-tag[data-note-id=' + id + ']');
  if ($tag.length) {
    $tag.css('zoom', 2);
    setTimeout(() => {$tag.css('zoom', 1);}, 1000);
  }
});

$(document).on('click', '[kepan]', function (e) {
  let $this = $(e.target),
      $p = $('.label-panel p:first-child'),
      id = $p.attr('id').substring(4),
      text = $p.text().split(': ');

  if ($this.find('.note-tag').length) return;
  $p.remove();
  $('<p class="note-p" data-note-id="' + id + '"><span class="org-text">' + text[1] +
    '</span><span class="note-text">' + text[2] + '</span></p>').insertAfter($this);
  $this.append($('<span class="note-tag" data-note-id="' + id + '" title="' + text[1] + '">' + noteTag + '</span>'));
});

// $('.note-tag').attr('title', null);
// $('.note-tag').css('zoom', null);
