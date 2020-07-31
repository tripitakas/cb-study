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