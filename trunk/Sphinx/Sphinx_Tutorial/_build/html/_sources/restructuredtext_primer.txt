.. _restructuredtext_primer:

******************************************
结构化文本入门(A reStructuredText Primer)
******************************************

:Author: Richard Jones
:Version: $Revision: 5801 $
:Copyright: This document has been placed in the public domain.
:原文:	http://docutils.sourceforge.net/docs/user/rst/quickstart.html
:翻译者: Qiu Karron (http://spaces.msn.com/karronqiu)
:翻译版本: $Revision: 4350 $
:修订者: Wu Lizong

.. contents:: 目录

.. |rst| replace:: :emphasis:`re`\ :strong:`Structured`\ :sup:`Text`

本文包含了一些类似于 "(quickref__)" 的链接. 他们指向了 `Quick reStructuredText`_ 用户快速参考. 
如果这些链接不能正常工作,请参考 `master quick reference`_ 文档.


__
.. _Quick reStructuredText: quickref.html
.. _master quick reference:
   http://docutils.sourceforge.net/docs/user/rst/quickref.html

.. Note:: This document is an informal introduction to
   reStructuredText.  The `下一步?`_ section below has links to
   further resources, including a formal reference.


结构(Structure)
================

首先我们说"结构化文本"(Structured Text)可能有一点儿用词不当。它更像使用了前后一致的规则的"松散的文本"(Relaxed Text)。
这些规则可以被一个HTML转换器转换为一个可以被Web浏览器浏览的非常结构化的文本。

被认为最基本的规则是段落(paragraph)(quickref__)。段落是被空行(一行就够了)分割的开的一段文字。段落必须有相同的缩进,也就是说,
他们必须左对齐。缩进的段落会导致缩进的引用段落 (Paragraphs that start indented will result in indented quote paragraphs.)。比如::

  This is a paragraph.  It's quite
  short.

     This paragraph will result in an indented block of
     text, typically used for quoting other text.

  This is another one.

显示结果是:

  This is a paragraph.  It's quite
  short.

     This paragraph will result in an indented block of
     text, typically used for quoting other text.

  This is another one.

__ quickref.html#paragraphs


文本样式(Text styles)
==================================

quickref__

__ quickref.html#inline-markup

在段落中或者其他文字块中,你可能会用 *italics* 来标记文本为斜体 "``*italics*``" ,
或者 **bold** 来标记粗体 "``**bold**``",这称为"内置标记"(inline markup) 。

如果你想显示为一个固定空格的文字,使用 "````两个反引号````".注意,
在两个反引号中的字符不会被处理,所以,"``*``" 之类的符号会保持原样。

如果你发现你想在文本中使用一个特殊字符,通常是可以的 --reStructuredText是足够聪明的。
例如,在公式5*6=30中,单星号会被处理的很好。如果你确实想让文字用\*括起来,而**不是**让它变成斜体,
那么你需要指出星号不是特殊字符。你可以在星号之前输入一个反斜杠,象这样 "``\*``" (quickref__),
或者用两个反引号(内置 literals),象这样::

    ``*``

__ quickref.html#escaping

.. Tip:: 内置标记(inline markup)可以理解为一种括号, 在文字的前面和后面成对出现,内置标记本身(前后都有空格)或位于文字间(or in the middle of a word)不会被显示.详情请参考 `markup spec`__ .

__ ../../ref/rst/restructuredtext.html#inline-markup


列表(Lists)
============

列表项主要有三种类型：**枚举** , **要点** 和 **定义** 。在所有的列表实例中,
你可以再列表中使用多个段落和子列表等,只要段落或者别的什么和列表项中第一行的文字左对齐就行。

列表必须总是开始于一个新的段落 --也就是说,他们必须在一个空行的后面。

**枚举** 列表 ( quickref__)
  __ quickref.html#enumerated-lists

  行的起始位置是数字,字符或者罗马字符,用一个数字或者字符再加上一个点“.”,右括号")"或者被括号"( )"括起来--任何你感到舒服的方法都行。下面所有的形式都可以被识别::

    1. 数字

    A. 大写字母
       使用多行

       并且分为两段!

    a. 小写字母

       3. 用不同的起始数字的子列表
       4. 请确认数字顺序的准确!

    I. 大写罗马字母

    i. 小写罗马字母

    (1) 又使用数字了

    1) 再来一次

  显示结果是 (注意:不是所有的Web浏览器都支持所有的枚举类型，所以你现在使用的浏览器无法看到我们所期望的效果):

  1. 数字

  A. 大写字母
     使用多行

     并且分为两段!

  a. 小写字母

    3. 用不同的起始数字的子列表
    4. 请确认数字顺序的准确!

  I. 大写罗马字母

  i. 小写罗马字母

  (1) 又使用数字了

  1) 再来一次

**要点** 列表 (quickref__)
  __ quickref.html#bullet-lists

  跟枚举列表类似,在行的起始处是圆点符号, 可以使用"-","+" 或者 "*"::

    * a bullet point using "*"

      - a sub-list using "-"

        + yet another sub-list

      - another item
	  
  显示结果是:

  * a bullet point using "*"

    - a sub-list using "-"

      + yet another sub-list

    - another item
	
**定义** 列表 (quickref__)
  __ quickref.html#definition-lists

  和其他两个不一样，定义列表包含了一个术语，还有术语的定义。定义列表的格式如下::

    what
      定义列表关联了一个术语和一个定义.

    *how*
	  术语是独占一行的词组,
	  定义是一个或多个段落或者正文元素,
	  缩进关联到定义上.
	  在术语和定义之间不允许有空行.

  显示结果是:

  what
    定义列表关联了一个术语和一个定义.

  *how*
	术语是独占一行的词组,
	定义是一个或多个段落或者正文元素,
	缩进关联到定义上.
	在术语和定义之间不允许有空行.

原始代码(示例代码)(Preformatting(Sample Codes))
==================================================
(quickref__)

__ quickref.html#literal-blocks

为了包含一大块原始代码，永远不会被篡改的文本，在前面的段落用"::"结尾。原始格式文本块结束于和前面的段落的缩进相同时。例如::

  An example::

      Whitespace, newlines, blank lines, and all kinds of markup
        (like *this* or \this) is preserved by literal blocks.
    Lookie here, I've dropped an indentation level
    (but not far enough)

  no more example

显示结果是:

  An example::

      Whitespace, newlines, blank lines, and all kinds of markup
        (like *this* or \this) is preserved by literal blocks.
    Lookie here, I've dropped an indentation level
    (but not far enough)

  no more example

注意，如果一个段落只包含"::",那么在输出的时候会被去掉,如::

  ::

      This is preformatted text, and the
      last "::" paragraph is removed

显示结果是:

::

    This is preformatted text, and the
    last "::" paragraph is removed


章节(Sections)
================

(quickref__)

__ quickref.html#section-structure

你可以使用 **章节标题** 将很长的文本划分为章节。用带修饰符的单行文字(一个或多个单词): 下划线，
或者同时具有下划线和上划线，单横线"``-------``", 等号"``==========``",波浪号"``~~~~~~~~~~~``"
或者任何你感到舒服的非字母数字的字符 ``= - ` : ' " ~ ^ _ * + # < >`` 。一个使用同样字符的下划线
修饰符与上下划线修饰符的区别很明显。上下划线必须至少一样长。他们是一致的，因为所有用同种修
饰符标记的章节都是处于同样的级别::

  Chapter 1 Title
  ===============

  Section 1.1 Title
  -----------------

  Subsection 1.1.1 Title
  ~~~~~~~~~~~~~~~~~~~~~~

  Section 1.2 Title
  -----------------

  Chapter 2 Title
  ===============

用简单的伪XML表示的结构为::

    <section>
        <title>
            Chapter 1 Title
        <section>
            <title>
                Section 1.1 Title
            <section>
                <title>
                    Subsection 1.1.1 Title
        <section>
            <title>
                Section 1.2 Title
    <section>
        <title>
            Chapter 2 Title

(伪XML使用缩进来表示嵌套，没有闭合标签。不可能在处理结果中显示出来，和其他例子一样，
因为章节不能在区块引用中存在。一个具体的例子，比较本文的源文件的章节结构和处理后的输出)

注意章节的标题可以使用他们的名称来作为连接对象。为了连接 列表(Lists) 的标题，
我写了 "``列表(Lists)_``" .如果标题有空格，象 `文本样式(Text styles)`_ 一样，
我们需要将标题引起来 "```文本样式(Text styles)`_``".



文档标题和子标题(Document Title/Subtitle)
------------------------------------------

整个文档的标题和章节标题区别很明显，可能会用不同的方式来格式化(例如HTML Writer默认会显示为一个居中的标题)。

在reStructuredText中标记一个文档标题，在文档的开头使用一个独一的修饰符。为了定义子标题，在文档标题之后使用另外的唯一的标识符。例如::

    ================
     Document Title
    ================
    ----------
     Subtitle
    ----------

    Section Title
    =============

    ...

注意，上面的"文档标题"和"章节标题"都使用等号，但是他们是有区别的和毫无关联的样式。
具有上划线和下划线的标题的文字(不仅仅使用下划线)可以为了美观的原因而插入。


图像(Images)
=============

(quickref__)

__ quickref.html#directives

为了在你的文档中包含图片，你可以使用 ``image`` 指令 directive_。例如::

  .. image:: images/sphinx_logo.png

results in:

.. image:: images/sphinx_logo.png

``images/sphinx_logo.png`` 部分指明了你希望在文档中显示的图片的文件名。没有限制图片的位置(格式，大小等)。
如果图片是用来在HTML中显示，你可能会希望提供一些附加的信息，你可以::

  .. image:: images/sphinx_logo.png
     :height: 115
     :width: 658
     :scale: 50
     :alt: Sphinx Logo

更多的信息，请查阅完整的 `image directive documentation`_ 文档.

__ ../../ref/rst/directives.html
__ ../../ref/rst/directives.html#images


下一步?
=============

本入门文档只包含了reStructuredText的最普通的特性，还有更多的东西需要探索。 
`Quick reStructuredText`_ 是进行下一步的好去处。完整的细节，可以参考 `reStructuredText Markup Specification`_ [#]_.

用户在使用Docutils 或 reStructuredText过程中如果有任何疑问或需要帮助，请到 Docutils-users_ 邮件列表中发信息进行咨询或求助.

.. [#] If that relative link doesn't work, try the master document:
   http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html.

.. _reStructuredText Markup Specification:
   ../../ref/rst/restructuredtext.html
.. _Docutils-users: ../mailing-lists.html#docutils-users
.. _Docutils project web site: http://docutils.sourceforge.net/
