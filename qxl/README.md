# 《大乘起信论》页面制作过程

本文说明《大乘起信论》新旧译本对照、内置科判导航、合并注论释的制作过程。

[操作结果网页](T1666-1667.html)

1. 从 [CBeta][CB] 网站下载《大乘起信论》[梁译][T1666] 和 [唐译][T1667] 的HTML文件：T1666.html、T1667.html。

   下载方法：点击“设定”按钮，开启与关闭系统外挂，启用“经文导出按钮”，然后“汇出”全部HTML。
   如果是多卷网页，则将其余网页中的`<div id='body'>`节点的所有文本(折叠节点后更方便复制)依次复制到第一个网页中。

2. 将这两个网页合并为一个文件：一卷梁译的`<div id='body'>`改为`<div id='body-left'>`，
   两卷唐译的第一个`<div id='body'>`改为`<div id='body-right'>`，删除其余的`</div><div id='body'>`。
   删除`cbeta-copyright`节点。
   
   然后运行 `python3 util/p_add_id.py qxl/T1666-1667.html`为每个段落分配编号，得到 `T1666-1667.html`。
   
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
   - 加 `<div class="label-panel">...</div>` 用于分组操作
   - 开始分组操作 `initGroupRows();`
   - 然后在两栏段落中依次单击段落，点击“移为一组”按钮，相应段落将移到红线上面的合并区内。
   - 如果段落需要拆分，就在网页中找到插入位置，插入`</p>`，换行插入`<p id='p82b'>`，其中的编号数字部分与上一段相同，末尾用字母区分。
     分组操作结束，或拆分段落前，将右边的段落分组内容复制到网页的 rowPairs 变量处，修改完成后刷新网页。

[CB]: http://cbetaonline.cn
[T1666]: http://cbetaonline.cn/zh/T1666_001
[T1667]: http://cbetaonline.cn/zh/T1667_001
