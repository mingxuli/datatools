HEADER
; IDL Visual Widget Builder Resource file. Version 1
; Generated on:	03/29/2008 20:50.32
VERSION 1
END

TopBase BASE 5 5 621 426
REALIZE "InitShow"
TLB
CAPTION "GIMMS Tools for ENVI"
XPAD = 3
YPAD = 3
SPACE = 3
BEGIN
  FilePath_TEXT TEXT 100 2 451 29
  EDITABLE
  WIDTH = 20
  HEIGHT = 1
  END
  FileSelect_BUTTON PUSHBUTTON 554 1 57 32
  VALUE "ѡ��"
  ALIGNCENTER
  ONACTIVATE "OpenGIMMS"
  END
  WID_LABEL_0 LABEL 3 10 96 20
  VALUE "GIMMS����Ŀ¼��"
  ALIGNLEFT
  END
  Main_BASE BASE 1 44 392 346
  XPAD = 3
  YPAD = 3
  SPACE = 3
  CAPTION "IDL"
  BEGIN
    Boundary_DROPLIST DROPLIST 90 2 290 25
    ONSELECT "Set_Boundary"
    END
    OutFormate_DROPLIST DROPLIST 98 225 287 26
    ONSELECT "Set_OutFormate"
    END
    WID_LABEL_5 LABEL 0 6 86 17
    VALUE "�����иΧ��"
    ALIGNRIGHT
    END
    Boundary_BASE BASE 5 37 378 176
    FRAME = 1
    XPAD = 3
    YPAD = 3
    SPACE = 3
    CAPTION "IDL"
    BEGIN
      WID_LABEL_1 LABEL 174 4 28 18
      VALUE "��"
      ALIGNLEFT
      END
      North_TEXT TEXT 132 29 109 31
      WIDTH = 20
      HEIGHT = 1
      END
      WID_LABEL_3 LABEL 335 87 31 18
      VALUE "��"
      ALIGNLEFT
      END
      WID_LABEL_2 LABEL 2 86 27 19
      VALUE "��"
      ALIGNRIGHT
      END
      West_TEXT TEXT 35 79 89 31
      WIDTH = 20
      HEIGHT = 1
      END
      WID_LABEL_4 LABEL 170 119 14 18
      VALUE "��"
      ALIGNLEFT
      END
      East_TEXT TEXT 236 79 94 31
      WIDTH = 20
      HEIGHT = 1
      END
      South_TEXT TEXT 128 136 110 31
      WIDTH = 20
      HEIGHT = 1
      END
    END
    WID_LABEL_6 LABEL 8 228 84 23
    VALUE "���������ʽ��"
    ALIGNLEFT
    END
    OutPath_TEXT TEXT 99 266 285 24
    EDITABLE
    WIDTH = 20
    HEIGHT = 1
    END
    Run_BUTTON PUSHBUTTON 52 306 88 33
    VALUE "����"
    ALIGNCENTER
    ONACTIVATE "Run"
    END
    Quit_BUTTON PUSHBUTTON 180 305 96 32
    VALUE "ȡ��"
    ALIGNCENTER
    ONACTIVATE "Cancle"
    END
    OutPath_BUTTON PUSHBUTTON 4 259 85 28
    VALUE "�������Ŀ¼"
    ALIGNCENTER
    ONACTIVATE "Set_Outpath"
    END
  END
  Message_BASE BASE 396 44 217 348
  XPAD = 3
  YPAD = 3
  SPACE = 3
  CAPTION "IDL"
  BEGIN
    Message_TEXT TEXT 1 4 213 342
    FRAME = 1
    SCROLL
    NONEWLINE
    WRAP
    WIDTH = 20
    HEIGHT = 1
    END
  END
END
