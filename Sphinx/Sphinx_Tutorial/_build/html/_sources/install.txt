.. _installing-docdir:


***************
Sphinx安装
***************

首选需要说明的是,本安装时在windows环境下执行的。如果你已经下载并安装了 `Sphinx <http://sphinx.pocoo.org/>`_
你可以在python环境下通过如下方式进行检验::

  >>> import sphinx
  
如果没有错误的提示，说明你已经正确安装。否则的话，请安装python的sphinx模块。sphinx没有提供windows .exe安装包，
必须通过easy_install工具进行安装。你可以通过 `Python Package Index <http://pypi.python.org/pypi/Sphinx>`_ 
下载 EGG文件进行安装,也可以直接在线安装::

  > easy_install -U Sphinx

现在你可以使用sphinx-quickstart命令建立你自己的文档模板了,不过在此之前你需要建立一个目录来存放你的文档，如（D:\Sphinx_Tutorial）,
进入目录，在命令窗口中执行命令::

  > sphinx-quickstart

然后回答相关的问题，如果你不知道该如何回答，可以直接按下回车键，接受默认设置. 本教程使用"Sphinx_Tutorial"作为文档工程的名称，
默认情况下创建的文件和文件夹如下::

  _build
  _static
  _templates
  conf.py
  index.rst
  make.bat
  Makefile

index.rst文件就是这个文档的首页,在开始编辑前，我们先看看默认的界面是什么样子的，直接编译成html格式，在DOS命令行中执行命令::

  > make html

点击浏览 :file:`d:\\Sphinx_Tutorial\\_build\\html\\index.html` 页面,你可以看到如下页面.

.. image:: _static/basic_screenshot.png
   :align: center
.. note::
   本教程使用的是Sphinx 1.0b2版,使用的Python是2.5版,如果你的版本跟本教程的版本不同,所出现的提示或结果可能也会不同。