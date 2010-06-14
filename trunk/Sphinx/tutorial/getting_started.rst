.. _getting_started:


***************
开始
***************

.. _installing-docdir:

安装
================

首选需要说明的是,本安装时在windows环境下执行的。如果你已经下载并安装了 `sphinx <http://sphinx.pocoo.org/>`_
你可以在python环境下通过如下方式进行检验::

  >>> import sphinx
  
如果没有错误的提示，说明你已经正确安装。否则的话，请安装python的sphinx模块。sphinx没有提供windows .exe安装包，必须通过easy_install工具进行安装。你可以通过`Python Package Index <http://pypi.python.org/pypi/Sphinx>`_ 下载 EGG文件进行安装,也可以直接在线安装::

  > easy_install -U Sphinx

现在你可以使用sphinx-quickstart命令建立你自己的文档模板了,不过在此之前你需要建立一个目录来存放你的文档，如（d:\sampledoc）, 进入目录，在命令窗口中执行命令::

  > sphinx-quickstart

然后回答相关的问题，如果你不知道该如何回答，可以直接按下回车键，接受默认设置. 本教程使用"sampledoc"作为文档工程的名称，默认情况下创建的文件和文件夹如下::

  _build
  _static
  _templates
  conf.py
  index.rst
  make.bat
  Makefile

index.rst文件就是这个文档的首页,在添加内容之前，我们先看看默认的界面是什么样子的，直接编译成html格式，在DOS命令行中执行命令::

  > make html

点击浏览 :file:`d:\\sampledoc\\_build\\html\\index.html` 页面,你可以看到如下页面.

.. image:: _static/basic_screenshot.png


.. _fetching-the-data:

下载实例代码
-----------------

Now we will start to customize out docs.  Grab a couple of files from
the `web site
<http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/sampledoc_tut/>`_
or svn.  You will need :file:`getting_started.rst` and
:file:`_static/basic_screenshot.png`.  All of the files live in the
"completed" version of this tutorial, but since this is a tutorial,
we'll just grab them one at a time, so you can learn what needs to be
changed where.  Since we have more files to come, I'm going to grab
the whole svn directory and just copy the files I need over for now.
First, I'll cd up back into the directory containing my project, check
out the "finished" product from svn, and then copy in just the files I
need into my :file:`sampledoc` directory::

  home:~/tmp/sampledoc> pwd
  /Users/jdhunter/tmp/sampledoc
  home:~/tmp/sampledoc> cd ..
  home:~/tmp> svn co https://matplotlib.svn.sourceforge.net/svnroot/\
  matplotlib/trunk/sampledoc_tut
  A    sampledoc_tut/cheatsheet.rst
  A    sampledoc_tut/_static
  A    sampledoc_tut/_static/basic_screenshot.png
  A    sampledoc_tut/conf.py
  A    sampledoc_tut/Makefile
  A    sampledoc_tut/_templates
  A    sampledoc_tut/_build
  A    sampledoc_tut/getting_started.rst
  A    sampledoc_tut/index.rst
  Checked out revision 7449.
  home:~/tmp> cp sampledoc_tut/getting_started.rst sampledoc/
  home:~/tmp> cp sampledoc_tut/_static/basic_screenshot.png \
  sampledoc/_static/

The last step is to modify :file:`index.rst` to include the
:file:`getting_started.rst` file (be careful with the indentation, the
"g" in "getting_started" should line up with the ':' in ``:maxdepth``::

  Contents:

  .. toctree::
     :maxdepth: 2

     getting_started.rst

and then rebuild the docs::

  cd sampledoc
  make html


When you reload the page by refreshing your browser pointing to
:file:`_build/html/index.html`, you should see a link to the
"Getting Started" docs, and in there this page with the screenshot.
`Voila!`

Note we used the image directive to include to the screenshot above
with::

  .. image:: _static/basic_screenshot.png


Next we'll customize the look and feel of our site to give it a logo,
some custom css, and update the navigation panels to look more like
the `sphinx <http://sphinx.pocoo.org/>`_ site itself -- see
:ref:`custom_look`.

