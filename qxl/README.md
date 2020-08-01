# 《大乘起信论》页面制作过程

本文说明《大乘起信论》新旧译本对照、内置科判导航、合并注论释的制作过程。

- [最终网页](T1666K.html)
- [第3步: 合并为两栏的页面](step3.html)
- [第4步: 段落分组两栏对照](step4.html)
- [第5步: 退出段落分组模式](step5.html)
- [第6步: 科判标引](step6.html)
- [第7步: 加导航条](step7.html)

1. 从 [CBeta][CB] 网站下载《大乘起信论》[梁译][T1666] 和 [唐译][T1667] 的HTML文件：T1666.html、T1667.html。

   下载方法：点击“设定”按钮，开启与关闭系统外挂，启用“经文导出按钮”，然后“汇出”全部HTML。
   如果是多卷网页，则将其余网页中的`<div id='body'>`节点的所有文本(折叠节点后更方便复制)依次复制到第一个网页中。

2. 将这两个网页合并为一个文件：一卷梁译的`<div id='body'>`改为`<div id='body-left'>`，
   两卷唐译的第一个`<div id='body'>`改为`<div id='body-right'>`，删除其余的`</div><div id='body'>`。
   删除`cbeta-copyright`节点。
   
   然后运行 `python3 util/p_add_id.py qxl/step5.html`为每个段落分配编号，得到 `step5.html`。
   
3. 将合并后的网页改为左右两栏的页面，加上 bootstrap、jquery、cb.css 的引用，将上面的 `<div id='body...>` 改造为：

    ```html
    <div id="content" class="container-fluid">
      <div class="row">
        <div class="original col-xs-6" id='body-left'...>
        <div class="original col-xs-6" id='body-right'...>
      </div>
    </div>
    ```

4. 段落分组，让两栏对照内容对应

   - 在网页中引用 `label-panel.css`、`group-rows.js`、`reader.js`
   - 加 `<div id="merged" class="container-fluid"></div>`，用于收集合并后的内容
   - 加 `<div class="label-panel">...</div>` （代码片段如下）用于分组操作。
   - 开始分组操作 `initGroupRows();`
   - 然后在两栏段落中依次单击段落，点击“移为一组”按钮，相应段落将移到红线上面的合并区内。
   - 如果段落需要拆分，就在网页中找到插入位置，插入`</p>`，换行插入`<p id='p82b'>`，其中的编号数字部分与上一段相同，末尾用字母区分。
     分组操作结束，或拆分段落前，将右边的段落分组内容复制到网页的 rowPairs 变量处，修改完成后刷新网页。

   ```html
    <div class="label-panel">
      <div class="current-row">
        <p>在左边红线下两栏中依次点击要同在一组的段落。</p>
        <div class="row">
          <label class="col-xs-2">左栏：</label>
          <div class="col-xs-10 row-left-ids"></div>
        </div>
        <div class="row">
          <label class="col-xs-2">右栏：</label>
          <div class="col-xs-10 row-right-ids"></div>
        </div>
        <button class="btn btn-default" id="move-row" title="将此组段落移到左上的合并区，成为左右对照的一组">移为一组</button>
      </div>
      <div class="row-pairs-div">
        <p>将下面内容复制到网页的 rowPairs 变量处。</p>
        <textarea readonly></textarea>
      </div>
    </div>
   ```

5. 退出段落分组标引模式：
   - 去掉 `label-panel.css`、`group-rows.js` 的引用
   - 删除 `<div class="label-panel">...</div>`
   - 将 `initGroupRows();` 改为 `rowPairs.split('||').forEach(movePairs);`
   - 后续发现有个别段落需要拆分或合并，可以直接修改 `rowPairs` 而不必进入段落分组标引模式。
     如需让某些段落（例如卷尾）默认隐藏，可在其编号处加减号，例如 `p67- | p129- ||`

6. 科判标引
   - 在前面得到的页面中复制`#merged`元素的HTML内容，覆盖到`#content`（删除`#merged`，改变`#content`），作为后续的正文`T1666K.html`。
     删除`rowPairs`及其函数调用。

   - 制作科判内容
     - 在MindNode等思维导图软件中编辑科判内容，导出 OPML 格式文件。
     - 使用 [opml-to-json][opml-to-json] 工具转为JSON格式的文件，其中有`title`和`children`节点。
       或者使用 [xml-to-json][xml-to-json] 在线转为JSON，替换节点名。
     - 使用 `util/set_tree_id.py` 脚本为科判节点分配编号，将生成的`_tree.json`参考`T1666K.json.js`格式完成科判JSON的制作。

   - 在页面加入 `.left-nav#judgments` 和 `footer` 元素，参考相关典籍开始科判标引：
     依次选中论文文本，点击科判节点，即将此文本提取为一个span，并设置其科判编号。允许有多个相同科判号的相邻span。
     不断重复此过程，完成(或部分完成)后复制`#content`元素的整个HTML内容到网页文件。

   - 最后退出科判标引，检查科判标引：
     - 注掉 `changed.jstree` 响应函数中的 `convertToSpanWithTag('kepan', data.node.id, data.node.text);`，
       换成 `highlightJudg(data.node.id, 'nav');`，这样在左边导航栏点击科判节点将高亮正文的响应内容。
     - 鼠标在正文有科判标记处滑过，在状态栏能看到两栏的科判标记数量，如果数量不一致可调整网页。
     - 数量一致时鼠标滑过会左右同步高亮显示。

7. 加顶部导航条，成为方便阅读的页面
   - 见页面的 `<nav class="navbar navbar-default navbar-fixed-top"...>` 部分

8. 合并注解到论文，将《義記》《裂網疏》的相关注解插入论文中。
   - 按步骤1下载并合并论疏网页 `T1846_001.html` 和 `T1850_001.html`
   - 将论疏网页的原文内容标记加粗，提取原文和注解到JSON文件：

     ```sh
     python util/mark_ori_bold.py qxl/T1846_001.html
     python util/extract_for_merge.py qxl/T1846_001-.html
     ```
   - 然后将JSON文件改为js文件（便于在HTML中静态加载），见`assets/T1846.json.js`的首行改动

   - 在页面引用这两个注解JSON文件和相关样式、标注用的脚本文件：

     ```html
     <link href="assets/note.css" rel="stylesheet"/>
     <link href="assets/label-panel.css" rel="stylesheet"/>

     <script src="assets/label-panel.js"></script>
     <script src="assets/T1846.json.js"></script>
     <script src="assets/T1850.json.js"></script>
     ```

     添加标注面板 `<div class="label-panel"><div></div></div>`。

     开始标注左列的义记注解：

     ```js
     $('#hide-kepan').click();
     initNotes(T1846Notes, '[義]', '.cell-l');
     // initNotes(T1850Notes, '[裂]', '.cell-r');
     ```

[CB]: http://cbetaonline.cn
[T1666]: http://cbetaonline.cn/zh/T1666_001
[T1667]: http://cbetaonline.cn/zh/T1667_001
[opml-to-json]: https://github.com/azu/opml-to-json
[xml-to-json]: https://www.convertjson.com/xml-to-json.htm
