# 《大乘起信论》页面制作过程

本文说明《大乘起信论》新旧译本对照、内置科判导航、合并注论释的制作过程。

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

[CB]: http://cbetaonline.cn
[T1666]: http://cbetaonline.cn/zh/T1666_001
[T1667]: http://cbetaonline.cn/zh/T1667_001
