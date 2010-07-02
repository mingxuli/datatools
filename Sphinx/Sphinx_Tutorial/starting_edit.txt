.. _starting_edit:


*******************
牛刀小试--修改主页
*******************

现在我们可以开始修改文档了，在此之前请下载本文档的代码，请从 `网站
<http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/sampledoc_tut/>`_
或通过svn下载. 现在你需要 :file:`getting_started.rst` 和 :file:`_static/basic_screenshot.png`.
所有的文件都在本文档的最终版本中,下面是所有文件的列表::

  A    sampledoc_tut/cheatsheet.rst
  A    sampledoc_tut/_static
  A    sampledoc_tut/_static/basic_screenshot.png
  A    sampledoc_tut/conf.py
  A    sampledoc_tut/Makefile
  A    sampledoc_tut/_templates
  A    sampledoc_tut/_build
  A    sampledoc_tut/getting_started.rst
  A    sampledoc_tut/index.rst

接下来是修改文件 :file:`index.rst`, 让他包含文件 :file:`getting_started.rst` ,修改的时候要注意，getting_started.rst的第一个字符g需要与:maxdepth: 2的第一个冒号对齐, 原始代码如下::

  Contents:

  .. toctree::
     :maxdepth: 2

     getting_started.rst

可以编译了，在命令行中，进入sampledoc文件夹，执行make 命令，编译为html格式的文档::

  cd sampledoc
  make html


刷新浏览器，或者打开文件 :file:`_build/html/index.html` ，你可以看到首页中已经链接了
"Getting Started" 文档，并且相关的标题也自动进入进来了，很神奇吧。

下一节我们将参照 `sphinx <http://sphinx.pocoo.org/>`_ 网站的样子，对我们的文档进行修改 -- 请参阅
:ref:`custom_look`.


