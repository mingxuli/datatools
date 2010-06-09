VERSION 5.00
Object = "{EAB22AC0-30C1-11CF-A7EB-0000C05BAE0B}#1.1#0"; "shdocvw.dll"
Object = "{831FDD16-0C5C-11D2-A9FC-0000F8754DA1}#2.0#0"; "mscomctl.ocx"
Begin VB.Form help 
   Caption         =   "帮助"
   ClientHeight    =   8205
   ClientLeft      =   60
   ClientTop       =   450
   ClientWidth     =   11295
   DrawMode        =   1  'Blackness
   BeginProperty Font 
      Name            =   "隶书"
      Size            =   15.75
      Charset         =   134
      Weight          =   700
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   Icon            =   "help.frx":0000
   LinkTopic       =   "Form1"
   ScaleHeight     =   8205
   ScaleWidth      =   11295
   StartUpPosition =   3  '窗口缺省
   Begin VB.PictureBox Picture1 
      Appearance      =   0  'Flat
      BackColor       =   &H8000000D&
      BorderStyle     =   0  'None
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   9
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000008&
      Height          =   735
      Left            =   0
      ScaleHeight     =   735
      ScaleWidth      =   8505
      TabIndex        =   0
      Top             =   0
      Width           =   8505
      Begin MSComctlLib.ImageList ImageList1 
         Left            =   4200
         Top             =   120
         _ExtentX        =   1005
         _ExtentY        =   1005
         BackColor       =   -2147483643
         ImageWidth      =   24
         ImageHeight     =   25
         MaskColor       =   12632256
         _Version        =   393216
         BeginProperty Images {2C247F25-8591-11D1-B16A-00C0F0283628} 
            NumListImages   =   1
            BeginProperty ListImage1 {2C247F27-8591-11D1-B16A-00C0F0283628} 
               Picture         =   "help.frx":038A
               Key             =   ""
            EndProperty
         EndProperty
      End
      Begin MSComctlLib.Toolbar Toolbar1 
         Height          =   465
         Left            =   120
         TabIndex        =   5
         ToolTipText     =   "返回首页"
         Top             =   120
         Width           =   495
         _ExtentX        =   873
         _ExtentY        =   820
         ButtonWidth     =   820
         ButtonHeight    =   820
         Appearance      =   1
         Style           =   1
         ImageList       =   "ImageList1"
         _Version        =   393216
         BeginProperty Buttons {66833FE8-8583-11D1-B16A-00C0F0283628} 
            NumButtons      =   1
            BeginProperty Button1 {66833FEA-8583-11D1-B16A-00C0F0283628} 
               ImageIndex      =   1
            EndProperty
         EndProperty
      End
      Begin VB.Timer Timer1 
         Interval        =   400
         Left            =   1680
         Top             =   480
      End
      Begin VB.Label Label2 
         BackStyle       =   0  'Transparent
         Caption         =   "Label2"
         Height          =   375
         Left            =   800
         TabIndex        =   2
         Top             =   200
         Width           =   5775
      End
      Begin VB.Image Image1 
         Appearance      =   0  'Flat
         Height          =   240
         Left            =   6120
         Picture         =   "help.frx":0AE6
         Top             =   240
         Width           =   240
      End
      Begin VB.Label Label1 
         Appearance      =   0  'Flat
         BackColor       =   &H80000005&
         BackStyle       =   0  'Transparent
         Caption         =   "Label1"
         BeginProperty Font 
            Name            =   "隶书"
            Size            =   18
            Charset         =   134
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         ForeColor       =   &H00FFFFFF&
         Height          =   375
         Left            =   6360
         TabIndex        =   1
         Top             =   165
         Width           =   1935
      End
   End
   Begin VB.Frame Frame1 
      BackColor       =   &H80000003&
      Height          =   8535
      Left            =   1440
      TabIndex        =   3
      Top             =   5520
      Width           =   11055
      Begin MSComctlLib.ListView ListView1 
         Height          =   2055
         Left            =   480
         TabIndex        =   13
         Top             =   720
         Width           =   3855
         _ExtentX        =   6800
         _ExtentY        =   3625
         View            =   1
         Arrange         =   1
         LabelEdit       =   1
         LabelWrap       =   -1  'True
         HideSelection   =   -1  'True
         FullRowSelect   =   -1  'True
         HotTracking     =   -1  'True
         _Version        =   393217
         ForeColor       =   -2147483644
         BackColor       =   -2147483645
         Appearance      =   0
         NumItems        =   0
      End
      Begin VB.Line Line1 
         BorderColor     =   &H80000005&
         X1              =   0
         X2              =   10680
         Y1              =   3960
         Y2              =   3960
      End
      Begin VB.Label Label3 
         AutoSize        =   -1  'True
         BackStyle       =   0  'Transparent
         Caption         =   "请选择一个帮助主题"
         BeginProperty Font 
            Name            =   "宋体"
            Size            =   18
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         ForeColor       =   &H00FFFFFF&
         Height          =   360
         Left            =   120
         TabIndex        =   4
         Top             =   240
         Width           =   3240
      End
   End
   Begin VB.Frame Frame2 
      BackColor       =   &H80000003&
      Height          =   6255
      Left            =   0
      TabIndex        =   6
      Top             =   600
      Width           =   11295
      Begin SHDocVwCtl.WebBrowser Wbhelp 
         Height          =   2415
         Left            =   3780
         TabIndex        =   15
         Top             =   960
         Width           =   3375
         ExtentX         =   5953
         ExtentY         =   4260
         ViewMode        =   0
         Offline         =   0
         Silent          =   0
         RegisterAsBrowser=   0
         RegisterAsDropTarget=   1
         AutoArrange     =   0   'False
         NoClientEdge    =   0   'False
         AlignLeft       =   0   'False
         NoWebView       =   0   'False
         HideFileNames   =   0   'False
         SingleClick     =   0   'False
         SingleSelection =   0   'False
         NoFolders       =   0   'False
         Transparent     =   0   'False
         ViewID          =   "{0057D0E0-3573-11CF-AE69-08002B2E1262}"
         Location        =   ""
      End
      Begin VB.PictureBox Picture4 
         Appearance      =   0  'Flat
         BackColor       =   &H8000000D&
         BorderStyle     =   0  'None
         ForeColor       =   &H80000008&
         Height          =   495
         Left            =   3760
         ScaleHeight     =   495
         ScaleWidth      =   7455
         TabIndex        =   11
         Top             =   360
         Width           =   7455
         Begin MSComctlLib.Toolbar Toolbar2 
            Height          =   525
            Left            =   20
            TabIndex        =   14
            Top             =   0
            Width           =   495
            _ExtentX        =   873
            _ExtentY        =   926
            ButtonWidth     =   820
            ButtonHeight    =   820
            Appearance      =   1
            ImageList       =   "ImageList1"
            _Version        =   393216
            BeginProperty Buttons {66833FE8-8583-11D1-B16A-00C0F0283628} 
               NumButtons      =   1
               BeginProperty Button1 {66833FEA-8583-11D1-B16A-00C0F0283628} 
                  ImageIndex      =   1
               EndProperty
            EndProperty
         End
         Begin VB.Label Label10 
            AutoSize        =   -1  'True
            BackStyle       =   0  'Transparent
            Caption         =   "Label10"
            ForeColor       =   &H00FFFFFF&
            Height          =   315
            Left            =   600
            TabIndex        =   12
            Top             =   120
            Width           =   1260
         End
      End
      Begin VB.PictureBox Picture3 
         BackColor       =   &H8000000D&
         BorderStyle     =   0  'None
         Height          =   495
         Left            =   240
         ScaleHeight     =   495
         ScaleWidth      =   3465
         TabIndex        =   9
         Top             =   360
         Width           =   3460
         Begin VB.Label Label9 
            AutoSize        =   -1  'True
            BackColor       =   &H8000000D&
            BackStyle       =   0  'Transparent
            Caption         =   "Label9"
            BeginProperty Font 
               Name            =   "Arial"
               Size            =   10.5
               Charset         =   0
               Weight          =   700
               Underline       =   0   'False
               Italic          =   0   'False
               Strikethrough   =   0   'False
            EndProperty
            ForeColor       =   &H00FFFFFF&
            Height          =   240
            Left            =   120
            TabIndex        =   10
            Top             =   120
            Width           =   690
         End
      End
      Begin VB.PictureBox Picture2 
         BackColor       =   &H8000000A&
         FillColor       =   &H8000000E&
         Height          =   6015
         Left            =   3720
         MousePointer    =   9  'Size W E
         ScaleHeight     =   6015
         ScaleWidth      =   45
         TabIndex        =   8
         Top             =   240
         Width           =   40
      End
      Begin MSComctlLib.TreeView TreeView1 
         Height          =   3735
         Left            =   240
         TabIndex        =   7
         Top             =   960
         Width           =   3465
         _ExtentX        =   6112
         _ExtentY        =   6588
         _Version        =   393217
         Indentation     =   529
         LabelEdit       =   1
         LineStyle       =   1
         Style           =   7
         HotTracking     =   -1  'True
         SingleSel       =   -1  'True
         Appearance      =   1
         BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
            Name            =   "隶书"
            Size            =   14.25
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
      End
   End
End
Attribute VB_Name = "help"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Dim X As Double
Dim Y As Double
Dim mnode(5) As Node
Dim hppath As String
Private Const treevieww = 1230

Sub gongju()
'***********************************************************************
'************为treeview控件加入树形结构
'**********************************************************************
Set mnode(1) = TreeView1.Nodes.Add(, , "gjlann", "工具栏按钮的使用")
mnode(1).ForeColor = 16744576
    Set mnode(2) = TreeView1.Nodes.Add("gjlann", tvwChild, "fd", "放大地图")
    mnode(2).ForeColor = 16744576
        Set mnode(3) = TreeView1.Nodes.Add("fd", tvwChild, "", "操作按钮")
        mnode(3).ForeColor = 16744576
        Set mnode(3) = TreeView1.Nodes.Add("fd", tvwChild, "", "操作地图")
        mnode(3).ForeColor = 16744576
    Set mnode(2) = TreeView1.Nodes.Add("gjlann", tvwChild, "sx", "缩小地图")
    mnode(2).ForeColor = 16744576
        Set mnode(3) = TreeView1.Nodes.Add("sx", tvwChild, "", "操作按钮")
        mnode(3).ForeColor = 16744576
        Set mnode(3) = TreeView1.Nodes.Add("sx", tvwChild, "", "操作地图")
        mnode(3).ForeColor = 16744576
    Set mnode(2) = TreeView1.Nodes.Add("gjlann", tvwChild, "py", "平移地图")
    mnode(2).ForeColor = 16744576
    Set mnode(2) = TreeView1.Nodes.Add("gjlann", tvwChild, "qt", "返回全图")
    mnode(2).ForeColor = 16744576
End Sub
Sub xtjm()
Set mnode(1) = TreeView1.Nodes.Add(, , "xtjm", "系统界面")
mnode(1).ForeColor = 16744576
    Set mnode(2) = TreeView1.Nodes.Add("xtjm", tvwChild, , "菜单栏")
mnode(2).ForeColor = 16744576
    Set mnode(2) = TreeView1.Nodes.Add("xtjm", tvwChild, , "工具栏")
mnode(2).ForeColor = 16744576
    Set mnode(2) = TreeView1.Nodes.Add("xtjm", tvwChild, , "显示图形区域")
mnode(2).ForeColor = 16744576
    Set mnode(2) = TreeView1.Nodes.Add("xtjm", tvwChild, , "显示属性区域")
mnode(2).ForeColor = 16744576
    Set mnode(2) = TreeView1.Nodes.Add("xtjm", tvwChild, , "显示属性面板")
mnode(2).ForeColor = 16744576
    Set mnode(2) = TreeView1.Nodes.Add("xtjm", tvwChild, , "显示图层面板")
mnode(2).ForeColor = 16744576
    Set mnode(2) = TreeView1.Nodes.Add("xtjm", tvwChild, , "检索内容浏览区域")
mnode(2).ForeColor = 16744576
    Set mnode(2) = TreeView1.Nodes.Add("xtjm", tvwChild, , "状态栏")
mnode(2).ForeColor = 16744576
End Sub
Private Sub Form_Load()
hppath = App.Path + "\Help\"
Label1.Caption = "帮助中心"
Label2.Caption = "欢迎使用《中国冰川编目》系统帮助"
Label10.Caption = "内容浏览区"
Frame1.Top = 600
Frame1.Left = 0
ListView1.ListItems.Add , , "系统界面说明"
ListView1.ListItems.Add , , "怎样对地图进行浏览"
End Sub


Private Sub Form_Resize()
Picture1.Width = Me.Width
Label1.Left = Me.Width - Label1.Width
Image1.Left = Me.Width - Label1.Width - Image1.Width - 80
Frame1.Width = Me.Width
Frame1.Height = Me.Height - Picture1.Height
Frame2.Width = Me.Width
Frame2.Height = Frame1.Height
Picture2.Height = Frame2.Height
TreeView1.Height = Frame1.Height - Label9.Height - 1200
Wbhelp.Height = TreeView1.Height
Picture4.Width = Frame2.Width - Picture2.Width - Picture3.Width - 500
Wbhelp.Width = Picture4.Width
End Sub


Private Sub ListView1_Click()
Select Case ListView1.SelectedItem
    Case ListView1.ListItems(1)
        Frame1.Visible = False
        Frame2.Visible = True
        Label9.Caption = ListView1.ListItems(1)
        TreeView1.Nodes.Clear
        Call xtjm
        Wbhelp.Navigate (hppath + "dtjmsm.htm")
    Case ListView1.ListItems(2)
        Frame1.Visible = False
        Frame2.Visible = True
        Label9.Caption = ListView1.ListItems(2)
        TreeView1.Nodes.Clear
        Call gongju
        Wbhelp.Navigate (hppath + "gjlanshy.htm")
End Select
End Sub

Private Sub Picture2_MouseDown(Button As Integer, Shift As Integer, X As Single, Y As Single)
Picture2.BackColor = Picture3.BackColor
Picture2.Top = Picture4.Top
End Sub

Private Sub Picture2_MouseMove(Button As Integer, Shift As Integer, X As Single, Y As Single)
Picture2.ZOrder 0
Picture2.Refresh
If Button = 1 Then
    Picture2.Left = Picture2.Left + X - 100
    If Picture2.Left > treevieww Then
        Picture2.Refresh
    Else
        Picture2.Left = treevieww
        Picture2.Left = Picture2.Left + X
        Picture2_MouseUp Button, Shift, X, Y
    End If
End If
End Sub

Private Sub Picture2_MouseUp(Button As Integer, Shift As Integer, X As Single, Y As Single)
Picture2.BackColor = -2147483638
TreeView1.Width = Picture2.Left - 260
Picture3.Width = TreeView1.Width
Picture4.Left = Picture2.Left - Picture2.Width + 100
Label9.Width = TreeView1.Width
Wbhelp.Left = Picture2.Left + Picture2.Width
Wbhelp.Width = Me.Width - TreeView1.Width - Picture2.Width - 480
Picture4.Width = Wbhelp.Width
End Sub

Private Sub Timer1_Timer()
Dim mr, mo, mb
Dim mx, my As Single
Dim mCurrX, mCurrY As Long
Dim mCurrDate As Date
Dim mCurrTime As Date

mr = Math.Rnd * 255
mo = Math.Rnd * 255
mb = Math.Rnd * 255
Label2.ForeColor = RGB(mr, mo, mb)
mx = mCurrX
my = mCurrY

End Sub


Private Sub Toolbar1_ButtonClick(ByVal Button As MSComctlLib.Button)
Frame2.Visible = False
Frame1.Visible = True
End Sub

Private Sub Toolbar2_ButtonClick(ByVal Button As MSComctlLib.Button)
If Label9.Caption = "系统界面说明" Then
    Wbhelp.Navigate (hppath + "dtjmsm.htm")
ElseIf Label9.Caption = "怎样对地图进行浏览" Then
    Wbhelp.Navigate (hppath + "gjlanshy.htm")
End If
End Sub

Private Sub TreeView1_NodeClick(ByVal Node As MSComctlLib.Node)
If Label9.Caption = "怎样对地图进行浏览" Then
    Select Case Node
        Case "工具栏按钮的使用"
            Wbhelp.Navigate (hppath + "gjlanshy.htm")
        Case "放大地图"
            Wbhelp.Navigate (hppath + "fddt.htm")
    End Select
ElseIf Label9.Caption = "系统界面说明" Then
    Select Case Node
        Case "系统界面"
            Wbhelp.Navigate (hppath + "dtjmsm.htm")
        Case "菜单栏"
            Wbhelp.Navigate (hppath + "caidanl.htm")
        Case "工具栏"
            Wbhelp.Navigate (hppath + "gongjul.htm")
        Case "显示图形区域"
            Wbhelp.Navigate (hppath + "txllqy.htm")
        Case "显示属性区域"
            Wbhelp.Navigate (hppath + "xianshishx.htm")
        Case "显示属性面板"
            Wbhelp.Navigate (hppath + "xshsx.htm")
        Case "显示图层面板"
            Wbhelp.Navigate (hppath + "xshtxmb.htm")
        Case "检索内容浏览区域"
            Wbhelp.Navigate (hppath + "jiansnr.htm")
        Case "状态栏"
            Wbhelp.Navigate (hppath + "zhuangtl.htm")
    End Select
End If
End Sub
