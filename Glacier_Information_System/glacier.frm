VERSION 5.00
Object = "{9BD6A640-CE75-11D1-AF04-204C4F4F5020}#2.0#0"; "MO20.OCX"
Object = "{C7FC2F7C-0688-11D5-B2F8-000102D87123}#1.0#0"; "MO21LEGEND.OCX"
Object = "{831FDD16-0C5C-11D2-A9FC-0000F8754DA1}#2.0#0"; "MSCOMCTL.OCX"
Object = "{6C20C089-0689-11D5-B2F8-000102D87123}#2.0#0"; "MO21SCALEBAR.OCX"
Object = "{F9043C88-F6F2-101A-A3C9-08002B2F49FB}#1.2#0"; "COMDLG32.OCX"
Object = "{BDC217C8-ED16-11CD-956C-0000C04E4C0A}#1.1#0"; "TABCTL32.OCX"
Begin VB.Form frmmain 
   BorderStyle     =   3  'Fixed Dialog
   Caption         =   "中国冰川编目(新)"
   ClientHeight    =   7245
   ClientLeft      =   2415
   ClientTop       =   2385
   ClientWidth     =   10725
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   MinButton       =   0   'False
   PaletteMode     =   1  'UseZOrder
   Picture         =   "glacier.frx":0000
   ScaleHeight     =   7245
   ScaleWidth      =   10725
   ShowInTaskbar   =   0   'False
   Begin VB.Frame Frame1 
      Height          =   1215
      Left            =   2280
      TabIndex        =   11
      Top             =   480
      Width           =   8415
      Begin MSComctlLib.ListView ListView1 
         Height          =   735
         Left            =   0
         TabIndex        =   12
         Top             =   480
         Width           =   8415
         _ExtentX        =   14843
         _ExtentY        =   1296
         View            =   3
         LabelEdit       =   1
         LabelWrap       =   -1  'True
         HideSelection   =   -1  'True
         FullRowSelect   =   -1  'True
         _Version        =   393217
         ForeColor       =   -2147483640
         BackColor       =   -2147483643
         Appearance      =   0
         NumItems        =   0
      End
      Begin VB.Label Label1 
         Appearance      =   0  'Flat
         BackColor       =   &H80000006&
         BackStyle       =   0  'Transparent
         Caption         =   "Label1"
         BeginProperty Font 
            Name            =   "宋体"
            Size            =   12
            Charset         =   134
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         ForeColor       =   &H00FF00FF&
         Height          =   495
         Left            =   0
         TabIndex        =   13
         Top             =   120
         Width           =   4455
      End
   End
   Begin VB.ListBox List4 
      Height          =   1320
      Left            =   5880
      TabIndex        =   33
      Top             =   4800
      Width           =   855
   End
   Begin VB.ListBox List3 
      Height          =   1680
      ItemData        =   "glacier.frx":4F5A
      Left            =   7080
      List            =   "glacier.frx":4F5C
      TabIndex        =   32
      Top             =   2400
      Width           =   975
   End
   Begin VB.TextBox Text1 
      Height          =   855
      Left            =   3600
      TabIndex        =   31
      Text            =   "Text1"
      Top             =   3240
      Width           =   1575
   End
   Begin VB.ListBox List2 
      Height          =   1860
      Left            =   5400
      TabIndex        =   30
      Top             =   2400
      Width           =   1095
   End
   Begin MSComDlg.CommonDialog CommonDialog1 
      Left            =   8400
      Top             =   0
      _ExtentX        =   847
      _ExtentY        =   847
      _Version        =   393216
   End
   Begin MSComctlLib.ListView datavw 
      Height          =   6465
      Left            =   2205
      TabIndex        =   4
      Top             =   360
      Width           =   8490
      _ExtentX        =   14975
      _ExtentY        =   11404
      View            =   3
      MultiSelect     =   -1  'True
      LabelWrap       =   -1  'True
      HideSelection   =   0   'False
      AllowReorder    =   -1  'True
      FullRowSelect   =   -1  'True
      HotTracking     =   -1  'True
      HoverSelection  =   -1  'True
      _Version        =   393217
      ForeColor       =   -2147483640
      BackColor       =   -2147483643
      Appearance      =   1
      NumItems        =   0
   End
   Begin MSComctlLib.StatusBar StatusBar1 
      Align           =   2  'Align Bottom
      Height          =   405
      Left            =   0
      TabIndex        =   8
      Top             =   6840
      Width           =   10725
      _ExtentX        =   18918
      _ExtentY        =   714
      _Version        =   393216
      BeginProperty Panels {8E3867A5-8586-11D1-B16A-00C0F0283628} 
         NumPanels       =   5
         BeginProperty Panel1 {8E3867AB-8586-11D1-B16A-00C0F0283628} 
            AutoSize        =   1
            Bevel           =   2
            Object.Width           =   5292
            MinWidth        =   5292
            Text            =   "中国冰川编目"
            TextSave        =   "中国冰川编目"
         EndProperty
         BeginProperty Panel2 {8E3867AB-8586-11D1-B16A-00C0F0283628} 
            AutoSize        =   1
            Bevel           =   2
            Object.Width           =   3529
            MinWidth        =   3529
         EndProperty
         BeginProperty Panel3 {8E3867AB-8586-11D1-B16A-00C0F0283628} 
            AutoSize        =   1
            Bevel           =   2
            Object.Width           =   5822
            MinWidth        =   5822
         EndProperty
         BeginProperty Panel4 {8E3867AB-8586-11D1-B16A-00C0F0283628} 
            Style           =   6
            Object.Width           =   2646
            MinWidth        =   2646
            TextSave        =   "04-4-9"
         EndProperty
         BeginProperty Panel5 {8E3867AB-8586-11D1-B16A-00C0F0283628} 
            Style           =   5
            AutoSize        =   1
            Object.Width           =   1764
            MinWidth        =   1764
            TextSave        =   "17:42"
         EndProperty
      EndProperty
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "宋体"
         Size            =   9
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
   End
   Begin VB.PictureBox Picture1 
      BorderStyle     =   0  'None
      Height          =   6405
      Left            =   2160
      MousePointer    =   9  'Size W E
      ScaleHeight     =   6405
      ScaleWidth      =   60
      TabIndex        =   5
      Top             =   360
      Width           =   60
   End
   Begin TabDlg.SSTab SSTab1 
      Height          =   6585
      Left            =   0
      TabIndex        =   1
      Top             =   360
      Width           =   2175
      _ExtentX        =   3836
      _ExtentY        =   11615
      _Version        =   393216
      Tabs            =   2
      Tab             =   1
      TabsPerRow      =   2
      TabHeight       =   882
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "宋体"
         Size            =   11.25
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      TabCaption(0)   =   "显示属性"
      TabPicture(0)   =   "glacier.frx":4F5E
      Tab(0).ControlEnabled=   0   'False
      Tab(0).Control(0)=   "datatv"
      Tab(0).ControlCount=   1
      TabCaption(1)   =   "显示图层"
      TabPicture(1)   =   "glacier.frx":4F7A
      Tab(1).ControlEnabled=   -1  'True
      Tab(1).Control(0)=   "maple"
      Tab(1).Control(0).Enabled=   0   'False
      Tab(1).Control(1)=   "List1"
      Tab(1).Control(1).Enabled=   0   'False
      Tab(1).Control(2)=   "Command1"
      Tab(1).Control(2).Enabled=   0   'False
      Tab(1).ControlCount=   3
      Begin VB.CommandButton Command1 
         Caption         =   "Command1"
         BeginProperty Font 
            Name            =   "宋体"
            Size            =   14.25
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   40
         TabIndex        =   10
         Top             =   3600
         Width           =   2055
      End
      Begin VB.ListBox List1 
         Height          =   2400
         Left            =   45
         Sorted          =   -1  'True
         TabIndex        =   9
         Top             =   3960
         Width           =   2055
      End
      Begin MO21legend.legend maple 
         Height          =   6000
         Left            =   0
         TabIndex        =   3
         Top             =   480
         Width           =   2100
         _ExtentX        =   3704
         _ExtentY        =   10583
         BackColor       =   -2147483644
         ForeColor       =   -2147483630
         BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
            Name            =   "MS Sans Serif"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
      End
      Begin MSComctlLib.TreeView datatv 
         Height          =   6015
         Left            =   -75000
         TabIndex        =   2
         Top             =   480
         Width           =   2115
         _ExtentX        =   3731
         _ExtentY        =   10610
         _Version        =   393217
         Indentation     =   176
         LabelEdit       =   1
         LineStyle       =   1
         Style           =   6
         SingleSel       =   -1  'True
         Appearance      =   1
      End
   End
   Begin MSComctlLib.ImageList ImageList1 
      Left            =   7440
      Top             =   0
      _ExtentX        =   1005
      _ExtentY        =   1005
      BackColor       =   -2147483643
      ImageWidth      =   16
      ImageHeight     =   16
      MaskColor       =   12632256
      _Version        =   393216
      BeginProperty Images {2C247F25-8591-11D1-B16A-00C0F0283628} 
         NumListImages   =   15
         BeginProperty ListImage1 {2C247F27-8591-11D1-B16A-00C0F0283628} 
            Picture         =   "glacier.frx":4F96
            Key             =   ""
         EndProperty
         BeginProperty ListImage2 {2C247F27-8591-11D1-B16A-00C0F0283628} 
            Picture         =   "glacier.frx":50A8
            Key             =   ""
         EndProperty
         BeginProperty ListImage3 {2C247F27-8591-11D1-B16A-00C0F0283628} 
            Picture         =   "glacier.frx":51BA
            Key             =   ""
         EndProperty
         BeginProperty ListImage4 {2C247F27-8591-11D1-B16A-00C0F0283628} 
            Picture         =   "glacier.frx":52CC
            Key             =   ""
         EndProperty
         BeginProperty ListImage5 {2C247F27-8591-11D1-B16A-00C0F0283628} 
            Picture         =   "glacier.frx":581E
            Key             =   ""
         EndProperty
         BeginProperty ListImage6 {2C247F27-8591-11D1-B16A-00C0F0283628} 
            Picture         =   "glacier.frx":5930
            Key             =   ""
         EndProperty
         BeginProperty ListImage7 {2C247F27-8591-11D1-B16A-00C0F0283628} 
            Picture         =   "glacier.frx":5C84
            Key             =   ""
         EndProperty
         BeginProperty ListImage8 {2C247F27-8591-11D1-B16A-00C0F0283628} 
            Picture         =   "glacier.frx":5FD8
            Key             =   ""
         EndProperty
         BeginProperty ListImage9 {2C247F27-8591-11D1-B16A-00C0F0283628} 
            Picture         =   "glacier.frx":60EA
            Key             =   ""
         EndProperty
         BeginProperty ListImage10 {2C247F27-8591-11D1-B16A-00C0F0283628} 
            Picture         =   "glacier.frx":643E
            Key             =   ""
         EndProperty
         BeginProperty ListImage11 {2C247F27-8591-11D1-B16A-00C0F0283628} 
            Picture         =   "glacier.frx":6792
            Key             =   ""
         EndProperty
         BeginProperty ListImage12 {2C247F27-8591-11D1-B16A-00C0F0283628} 
            Picture         =   "glacier.frx":6AE6
            Key             =   ""
         EndProperty
         BeginProperty ListImage13 {2C247F27-8591-11D1-B16A-00C0F0283628} 
            Picture         =   "glacier.frx":6BF8
            Key             =   ""
         EndProperty
         BeginProperty ListImage14 {2C247F27-8591-11D1-B16A-00C0F0283628} 
            Picture         =   "glacier.frx":6D0A
            Key             =   ""
         EndProperty
         BeginProperty ListImage15 {2C247F27-8591-11D1-B16A-00C0F0283628} 
            Picture         =   "glacier.frx":6E1C
            Key             =   ""
         EndProperty
      EndProperty
   End
   Begin MSComctlLib.Toolbar Toolbar1 
      Height          =   390
      Left            =   0
      TabIndex        =   0
      Top             =   0
      Width           =   6240
      _ExtentX        =   11007
      _ExtentY        =   688
      ButtonWidth     =   609
      ButtonHeight    =   582
      ImageList       =   "ImageList1"
      _Version        =   393216
      BeginProperty Buttons {66833FE8-8583-11D1-B16A-00C0F0283628} 
         NumButtons      =   16
         BeginProperty Button1 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            ImageIndex      =   1
         EndProperty
         BeginProperty Button2 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            ImageIndex      =   2
         EndProperty
         BeginProperty Button3 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            Style           =   3
         EndProperty
         BeginProperty Button4 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            ImageIndex      =   3
         EndProperty
         BeginProperty Button5 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            Style           =   3
         EndProperty
         BeginProperty Button6 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            ImageIndex      =   4
         EndProperty
         BeginProperty Button7 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            ImageIndex      =   5
         EndProperty
         BeginProperty Button8 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            ImageIndex      =   7
         EndProperty
         BeginProperty Button9 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            ImageIndex      =   6
         EndProperty
         BeginProperty Button10 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            ImageIndex      =   8
            Style           =   2
         EndProperty
         BeginProperty Button11 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            ImageIndex      =   9
            Style           =   2
         EndProperty
         BeginProperty Button12 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            ImageIndex      =   11
            Style           =   2
         EndProperty
         BeginProperty Button13 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            ImageIndex      =   12
            Style           =   2
         EndProperty
         BeginProperty Button14 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            ImageIndex      =   13
            Style           =   2
         EndProperty
         BeginProperty Button15 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            ImageIndex      =   14
            Style           =   2
         EndProperty
         BeginProperty Button16 {66833FEA-8583-11D1-B16A-00C0F0283628} 
            ImageIndex      =   15
            Style           =   2
         EndProperty
      EndProperty
      Begin MO21ScaleBar.ScaleBar ScaleBar1 
         Height          =   5000
         Left            =   8280
         TabIndex        =   7
         Top             =   0
         Width           =   300
         _ExtentX        =   529
         _ExtentY        =   8811
         BackColor       =   -2147483633
         BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
            Name            =   "MS Sans Serif"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
      End
   End
   Begin VB.Frame FLcolor 
      Caption         =   "Frame2"
      Height          =   4335
      Left            =   3120
      TabIndex        =   14
      Top             =   1080
      Width           =   4335
      Begin VB.CommandButton COk 
         Caption         =   "确定"
         Height          =   495
         Left            =   3120
         TabIndex        =   29
         Top             =   3720
         Width           =   975
      End
      Begin VB.CommandButton CCancel 
         Caption         =   "取消"
         Height          =   495
         Left            =   1680
         TabIndex        =   28
         Top             =   3720
         Width           =   975
      End
      Begin VB.CommandButton CApply 
         Caption         =   "显示"
         Height          =   495
         Left            =   480
         TabIndex        =   27
         Top             =   3720
         Width           =   855
      End
      Begin VB.TextBox TSize 
         Height          =   375
         Left            =   2400
         TabIndex        =   26
         Text            =   "Text2"
         Top             =   3120
         Width           =   615
      End
      Begin VB.ComboBox Cblayer 
         Height          =   300
         Left            =   2160
         TabIndex        =   24
         Text            =   "Combo1"
         Top             =   2640
         Width           =   1815
      End
      Begin VB.PictureBox Pline 
         Height          =   255
         Left            =   2760
         ScaleHeight     =   195
         ScaleWidth      =   915
         TabIndex        =   22
         Top             =   2040
         Width           =   975
      End
      Begin VB.PictureBox Player 
         Height          =   255
         Left            =   2760
         ScaleHeight     =   195
         ScaleWidth      =   915
         TabIndex        =   20
         Top             =   1440
         Width           =   975
      End
      Begin VB.TextBox TName 
         Height          =   375
         Left            =   2040
         TabIndex        =   18
         Top             =   720
         Width           =   2175
      End
      Begin VB.PictureBox Picture2 
         Appearance      =   0  'Flat
         BackColor       =   &H80000005&
         BorderStyle     =   0  'None
         ForeColor       =   &H80000008&
         Height          =   495
         Left            =   0
         Picture         =   "glacier.frx":6F2E
         ScaleHeight     =   495
         ScaleWidth      =   4335
         TabIndex        =   15
         Top             =   0
         Width           =   4335
         Begin VB.Image Image1 
            Appearance      =   0  'Flat
            Height          =   480
            Left            =   50
            Picture         =   "glacier.frx":1A4D2
            Top             =   30
            Width           =   480
         End
         Begin VB.Label Label2 
            Appearance      =   0  'Flat
            BackColor       =   &H80000005&
            BackStyle       =   0  'Transparent
            Caption         =   "Label2"
            BeginProperty Font 
               Name            =   "宋体"
               Size            =   9
               Charset         =   134
               Weight          =   700
               Underline       =   0   'False
               Italic          =   0   'False
               Strikethrough   =   0   'False
            EndProperty
            ForeColor       =   &H00FFFFFF&
            Height          =   495
            Left            =   720
            TabIndex        =   16
            Top             =   160
            Width           =   4335
         End
      End
      Begin VB.Label LLline 
         Caption         =   "边线大小："
         BeginProperty Font 
            Name            =   "宋体"
            Size            =   14.25
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   480
         TabIndex        =   25
         Top             =   3120
         Width           =   1695
      End
      Begin VB.Label LLType 
         Caption         =   "图层类型："
         BeginProperty Font 
            Name            =   "宋体"
            Size            =   14.25
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   480
         TabIndex        =   23
         Top             =   2640
         Width           =   1695
      End
      Begin VB.Label LLOutlinecolor 
         Caption         =   "图层边线颜色："
         BeginProperty Font 
            Name            =   "宋体"
            Size            =   14.25
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   480
         TabIndex        =   21
         Top             =   2040
         Width           =   2295
      End
      Begin VB.Label LLColor 
         Caption         =   "图层颜色："
         BeginProperty Font 
            Name            =   "宋体"
            Size            =   14.25
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   480
         TabIndex        =   19
         Top             =   1440
         Width           =   1455
      End
      Begin VB.Label LLName 
         Caption         =   "图层名称："
         BeginProperty Font 
            Name            =   "宋体"
            Size            =   14.25
            Charset         =   134
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   480
         TabIndex        =   17
         Top             =   720
         Width           =   1455
      End
   End
   Begin MapObjects2.Map mapvw 
      Height          =   6435
      Left            =   2205
      TabIndex        =   6
      Top             =   390
      Width           =   8505
      _Version        =   131072
      _ExtentX        =   15002
      _ExtentY        =   11351
      _StockProps     =   225
      BackColor       =   16777215
      BorderStyle     =   1
      WindowMode      =   1
      Contents        =   "glacier.frx":1A7DC
   End
   Begin VB.Menu wenjian 
      Caption         =   "文件"
      Begin VB.Menu lingcunwei 
         Caption         =   "另存为"
      End
      Begin VB.Menu dayin 
         Caption         =   "打印"
      End
      Begin VB.Menu tuichu 
         Caption         =   "退出"
      End
   End
   Begin VB.Menu shujufenxi 
      Caption         =   "数据分析"
      Begin VB.Menu tongji 
         Caption         =   "统计"
      End
      Begin VB.Menu chaxun 
         Caption         =   "查询"
      End
      Begin VB.Menu baobiao 
         Caption         =   "报表"
      End
   End
   Begin VB.Menu shezhi 
      Caption         =   "设置"
      Begin VB.Menu xianshishuxing 
         Caption         =   "显示属性"
      End
      Begin VB.Menu xianshituceng 
         Caption         =   "显示图层"
      End
   End
   Begin VB.Menu bangzhu 
      Caption         =   "帮助"
      Begin VB.Menu neirong 
         Caption         =   "内容"
      End
      Begin VB.Menu guanyuwomen 
         Caption         =   "关于我们"
      End
   End
End
Attribute VB_Name = "frmmain"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Public oblayer As Object
Dim layer As MapLayer
Private Const fm_l = 1230          '定义datatv的最小宽度
Dim i As Integer                   '定义变量
Private Const fm_t = 850          '定义maple的最小宽度
Dim newrec As MapObjects2.Rectangle '为放大、缩小定义
Dim zoomOutRect As MapObjects2.Rectangle
Dim pot As New Point
Dim X As Double
Dim Y As Double
Dim mapwidth As Double, mapheight As Double '为放大、缩小定义
Public gl As MapObjects2.MapLayer
Private mnode As Node
Public rsGlacier As New ADODB.Recordset
Private exp As String
Dim re As Rectangle
Dim po As Polygon
Dim el As Ellipse
Dim rec As MapObjects2.Recordset '*******定义搜索变量
Dim recs As MapObjects2.Recordset
Dim aName As String
Dim aField As Object
Dim asting As String
Dim alayer As Object
Dim schre As Rectangle
Dim schpoly As MapObjects2.Recordset '*******************定义点击list控件地图显示
Dim shappoly As Object
Dim rect As Object
Dim layerName As Variant
Dim potext As String '*************定义显示字体在单一目标上
Dim locn As New Point
Dim lay As MapObjects2.MapLayer
Dim layerfill(7) As String
Dim con As ADODB.Connection
Dim strg As String
Dim strec As ADODB.Recordset
Dim recss As MapObjects2.Recordset
Dim strecc As ADODB.Recordset
Dim t(40) As Node
Dim tr(30) As Node
Dim strglacier As String
Dim strsecond As String


Sub mdb()
Set con = New ADODB.Connection
Set strecc = New ADODB.Recordset
Set strec = New ADODB.Recordset
strg = "provider=Microsoft.Jet.OLEDB.4.0;Data Source=" & App.Path & "\glacier.mdb;"
con.Open strg
End Sub

Private Sub listview_AddItem(ByRef RecSet As ADODB.Recordset)
'
Dim itemgla1 As ListItem

    Set itemgla1 = ListView1.ListItems.Add()
    itemgla1.Text = RecSet!fifth_id
    itemgla1.SubItems(1) = RecSet!GLACIER_ID
    itemgla1.SubItems(2) = RecSet!GLACIER_NA & " "
    itemgla1.SubItems(3) = RecSet!latitude & " "
    itemgla1.SubItems(4) = RecSet!Longitude & " "
    itemgla1.SubItems(5) = RecSet!TOPO_TYPE & " "
    itemgla1.SubItems(6) = RecSet!TOPO_YEAR & " "
    itemgla1.SubItems(7) = RecSet!MAP_SCALE & " "
    itemgla1.SubItems(8) = RecSet!PHOTO_TYPE & " "
    itemgla1.SubItems(9) = RecSet!PHOTO_SCAL & " "
    itemgla1.SubItems(10) = RecSet!PHOTO_YEAR & " "
    itemgla1.SubItems(11) = RecSet!TOTAL_AREA & " "
    itemgla1.SubItems(12) = RecSet!AREA_ACCUR & " "
    itemgla1.SubItems(13) = RecSet!AREA_EXPOS & " "
    itemgla1.SubItems(14) = RecSet!AREA_ABLAT & " "
    itemgla1.SubItems(15) = RecSet!MEAN_WIDTH & " "
    itemgla1.SubItems(16) = RecSet!MEAN_LENGT & " "
    itemgla1.SubItems(17) = RecSet!TOTAL_LENG & " "
    itemgla1.SubItems(18) = RecSet!EXP_LENGTH & " "
    itemgla1.SubItems(19) = RecSet!ABL_LENGTH & " "
    itemgla1.SubItems(20) = RecSet!EXP_ORIEN & " "
    itemgla1.SubItems(21) = RecSet!ABL_ORIEN & " "
    itemgla1.SubItems(22) = RecSet!HIGH_ALTIT & " "
    itemgla1.SubItems(23) = RecSet!MEAN_ALTIT & " "
    itemgla1.SubItems(24) = RecSet!LOW_ALTITU & " "
    itemgla1.SubItems(25) = RecSet!EXP_LOW_AL & " "
    itemgla1.SubItems(26) = RecSet!GLA_CLASS & " "
    itemgla1.SubItems(27) = RecSet!MORAINE & " "
    itemgla1.SubItems(28) = RecSet!SNOWLINE & " "
    itemgla1.SubItems(29) = RecSet!SNOWL_ACCU & " "
    itemgla1.SubItems(30) = RecSet!SNOWL_DATE & " "
    itemgla1.SubItems(31) = RecSet!MEAN_DEPTH & " "
    itemgla1.SubItems(32) = RecSet!DEPTH_ACCU & " "
    itemgla1.SubItems(33) = RecSet!ICE_VOLUME & " "
    
End Sub

Sub research()
    aName = "Featureid"
    For Each aField In rec.Fields
        If aField.Type = moString Then
            aName = aField.Name
            Exit For
        End If
    Next
    While Not rec.EOF
        asting = rec(aName).ValueAsString
            List1.AddItem asting
        rec.MoveNext
    Wend

End Sub


Private Sub datavw_AddItem(ByRef RecSet As ADODB.Recordset)

Dim itemgla As ListItem

    Set itemgla = datavw.ListItems.Add()
    itemgla.Text = RecSet!fifth_id
    itemgla.SubItems(1) = RecSet!GLACIER_ID
    itemgla.SubItems(2) = RecSet!GLACIER_NA & " "
    itemgla.SubItems(3) = RecSet!latitude & " "
    itemgla.SubItems(4) = RecSet!Longitude & " "
    itemgla.SubItems(5) = RecSet!TOPO_TYPE & " "
    itemgla.SubItems(6) = RecSet!TOPO_YEAR & " "
    itemgla.SubItems(7) = RecSet!MAP_SCALE & " "
    itemgla.SubItems(8) = RecSet!PHOTO_TYPE & " "
    itemgla.SubItems(9) = RecSet!PHOTO_SCAL & " "
    itemgla.SubItems(10) = RecSet!PHOTO_YEAR & " "
    itemgla.SubItems(11) = RecSet!TOTAL_AREA & " "
    itemgla.SubItems(12) = RecSet!AREA_ACCUR & " "
    itemgla.SubItems(13) = RecSet!AREA_EXPOS & " "
    itemgla.SubItems(14) = RecSet!AREA_ABLAT & " "
    itemgla.SubItems(15) = RecSet!MEAN_WIDTH & " "
    itemgla.SubItems(16) = RecSet!MEAN_LENGT & " "
    itemgla.SubItems(17) = RecSet!TOTAL_LENG & " "
    itemgla.SubItems(18) = RecSet!EXP_LENGTH & " "
    itemgla.SubItems(19) = RecSet!ABL_LENGTH & " "
    itemgla.SubItems(20) = RecSet!EXP_ORIEN & " "
    itemgla.SubItems(21) = RecSet!ABL_ORIEN & " "
    itemgla.SubItems(22) = RecSet!HIGH_ALTIT & " "
    itemgla.SubItems(23) = RecSet!MEAN_ALTIT & " "
    itemgla.SubItems(24) = RecSet!LOW_ALTITU & " "
    itemgla.SubItems(25) = RecSet!EXP_LOW_AL & " "
    itemgla.SubItems(26) = RecSet!GLA_CLASS & " "
    itemgla.SubItems(27) = RecSet!MORAINE & " "
    itemgla.SubItems(28) = RecSet!SNOWLINE & " "
    itemgla.SubItems(29) = RecSet!SNOWL_ACCU & " "
    itemgla.SubItems(30) = RecSet!SNOWL_DATE & " "
    itemgla.SubItems(31) = RecSet!MEAN_DEPTH & " "
    itemgla.SubItems(32) = RecSet!DEPTH_ACCU & " "
    itemgla.SubItems(33) = RecSet!ICE_VOLUME & " "
    
End Sub
Sub tt()
'************************************************************
'***********函数设置功能按钮不用时变灰
'************************************************************
For i = 5 To 16
    Toolbar1.Buttons(i).Enabled = False
Next
Toolbar1.Buttons(1).Enabled = False
Toolbar1.Buttons(2).Enabled = False
lingcunwei.Enabled = False
dayin.Enabled = False
End Sub
Sub ttt()
'************************************************************
'***********函数设置功能按钮使用时还原
'************************************************************
For i = 5 To 16
    Toolbar1.Buttons(i).Enabled = True
Next
Toolbar1.Buttons(1).Enabled = True
'Toolbar1.Buttons(2).Enabled = True
lingcunwei.Enabled = True
'dayin.Enabled = True

End Sub


Private Sub baobiao_Click()
tongji.Checked = False
lingcunwei.Checked = False
dayin.Checked = False
chaxun.Checked = False
baobiao.Checked = True
neirong.Checked = False
guanyuwomen.Checked = False
End Sub

Private Sub chaxun_Click()
tongji.Checked = False
lingcunwei.Checked = False
dayin.Checked = False
chaxun.Checked = True
baobiao.Checked = False
neirong.Checked = False
guanyuwomen.Checked = False
Frmresult.Show
End Sub

Private Sub Command1_Click()
List1.Visible = True
End Sub

Private Sub Command2_Click()
End Sub

Private Sub comok_Click()
frmexport.Visible = False
End Sub

Private Sub datatv_NodeClick(ByVal Node As MSComctlLib.Node)
Dim rsFifth As New ADODB.Recordset
Dim rsSecond As New ADODB.Recordset
Dim rsThird As New ADODB.Recordset
Dim rsForst As New ADODB.Recordset
Dim rsForth As New ADODB.Recordset
Dim adrc As New ADODB.Recordset


Dim rsf As Integer

Dim strthird As String
Dim strforth As String
Dim strfifth As String
Dim countgla As Integer
Set rsGlacier = Nothing
    strsecond = "select * from glacier.second where first_id='" & Node.Key & "'"
    rsSecond.Open strsecond, con, adOpenStatic, adLockOptimistic
    
    strthird = "select * from glacier.third where second_id='" & Node.Key & "'"
    rsThird.Open strthird, con, adOpenStatic, adLockOptimistic

    strforth = "select * from glacier.forth where third_id='" & Node.Key & "'"
    rsForth.Open strforth, con, adOpenStatic, adLockOptimistic
    
    strfifth = "select * from glacier.fifth where forth_id='" & Node.Key & "'"
    rsFifth.Open strfifth, con, adOpenStatic, adLockOptimistic

If datavw.Visible = True Then
    strglacier = "select * from glacier.glacier where fifth_id Like '" & Trim(Node.Key) & "%" & "'"
    rsGlacier.Open strglacier, con, adOpenStatic, adLockOptimistic
    countgla = rsGlacier.RecordCount
End If

If Node.Tag = "firstname" Then
    If Node.Children = 0 Then
        Do Until rsSecond.EOF
            If Node.Key = rsSecond!first_id Then
                Set mnode = datatv.Nodes.Add(Node.index, tvwChild, rsSecond!second_id)
                mnode.Text = rsSecond!Description
                mnode.Tag = "secondname"
            End If
            rsSecond.MoveNext
        Loop
    End If
End If
If Node.Tag = "secondname" Then
    If Node.Children = 0 Then
        Do Until rsThird.EOF
            If Node.Key = rsThird!second_id Then
                Set mnode = datatv.Nodes.Add(Node.index, tvwChild, rsThird!third_id)
                mnode.Text = rsThird!Description
                mnode.Tag = "thirdname"
            End If
        rsThird.MoveNext
        Loop
    End If
End If
If Node.Tag = "thirdname" Then
    If Node.Children = 0 Then
        Do Until rsForth.EOF
            If Node.Key = rsForth!third_id Then
                Set mnode = datatv.Nodes.Add(Node.index, tvwChild, rsForth!forth_id)
                mnode.Text = rsForth!Description
                mnode.Tag = "forthname"
            End If
            rsForth.MoveNext
        Loop
    End If
End If
If Node.Tag = "forthname" Then
    If Node.Children = 0 Then
    Do Until rsFifth.EOF
        If Node.Key = rsFifth!forth_id Then
            Set mnode = datatv.Nodes.Add(Node.index, tvwChild, rsFifth!fifth_id)
            mnode.Text = rsFifth!Description
            mnode.Tag = "fifthname"
        End If
        rsFifth.MoveNext
    Loop
    End If
End If
    datavw.ListItems.Clear
    Dim l As Integer
    If datavw.Visible = True Then
        Do While Not rsGlacier.EOF
            datavw_AddItem rsGlacier
            If IsNull(rsGlacier.Fields(2).Value) = False Then
            List2.AddItem rsGlacier.Fields(2)
            Else
            List2.AddItem ""
            End If
            If IsNull(rsGlacier.Fields(3).Value) = False Then
            List3.AddItem rsGlacier.Fields(3)
            Else
            List3.AddItem ""
            End If
            If IsNull(rsGlacier.Fields(4).Value) = False Then
            List4.AddItem rsGlacier.Fields(4)
            Else
            List4.AddItem ""
            End If
           rsGlacier.MoveNext
        Loop
    End If
'动态改变表单名称
frmmain.Caption = "中国冰川编目——" & Node.Text
StatusBar1.Panels(1).Text = "流域编码：" & Node.Key
StatusBar1.Panels(2).Text = "本区冰川" & countgla & "条"
StatusBar1.Panels(3).Width = 2500
StatusBar1.Panels(3).Text = "流域名称：" & Node.Text

'=================================================================================
End Sub


Private Sub dayin_Click()
frmprint.Show
tongji.Checked = False
lingcunwei.Checked = False
dayin.Checked = True
chaxun.Checked = False
baobiao.Checked = False
neirong.Checked = False
guanyuwomen.Checked = False
mapvw.PrintMap "mymap", "", True
End Sub

Private Sub Form_Initialize()
CreateKey "HKEY_CLASSES_ROOT\CLSID\{6D835690-900B-11D0-9484-00A0C91110ED}"
CreateKey "HKEY_CLASSES_ROOT\CLSID\{6D835690-900B-11D0-9484-00A0C91110ED}\InprocServer32"
SetStringValue "HKEY_CLASSES_ROOT\CLSID\{6D835690-900B-11D0-9484-00A0C91110ED}\InprocServer32", "", "C:\Program Files\Common Files\ESRI\MSSTDFMT.DLL"

End Sub

Private Sub Form_Load()
  Text1.Visible = False
  List2.Visible = False
  List4.Visible = False
  List3.Visible = False
  
tongji.Enabled = False
baobiao.Enabled = False


'****************************************************************
'*************************************** 添加图层
'****************************************************************
Dim dcn As New DataConnection
Dim dataname As Variant
Dim ttt(20) As Node
Dim tttt(80) As Node
Dim intwidth As Integer
    CommonDialog1.Filename = "glacier.jpg"

xianshishuxing.Checked = True
StatusBar1.Style = sbrNormal
FLcolor.Visible = False
    dcn.Database = spath("VECTOR")
    layerName = Array("glbasin", "GLACIER", "lake", "rivern", "road")
Set layer = New MapLayer
    Set layer.GeoDataset = dcn.FindGeoDataset(layerName(0))
    layer.Symbol.Color = RGB(189, 197, 175)
    mapvw.Layers.Add layer
    layer.Name = "中国地图"
Set layer = New MapLayer
    Set layer.GeoDataset = dcn.FindGeoDataset(layerName(3))
    layer.Symbol.Color = RGB(23, 60, 202)
    mapvw.Layers.Add layer
    layer.Name = "河流"
Set layer = New MapLayer
    Set layer.GeoDataset = dcn.FindGeoDataset(layerName(1))
    layer.Symbol.Color = RGB(255, 221, 102)
    mapvw.Layers.Add layer
    layer.Name = "冰川"
Set layer = New MapLayer
    Set layer.GeoDataset = dcn.FindGeoDataset(layerName(2))
    layer.Symbol.Color = RGB(66, 100, 234)
    mapvw.Layers.Add layer
    layer.Name = "湖泊"
Set layer = New MapLayer
    Set layer.GeoDataset = dcn.FindGeoDataset(layerName(4))
    layer.Symbol.Color = RGB(255, 26, 31)
    mapvw.Layers.Add layer
    layer.Name = "道路"
    SSTab1.Tab = 0
    tt
    Toolbar1.Buttons(11).Visible = False
    Toolbar1.Buttons(12).Visible = False
intwidth = datavw.Width / 6
'以下代码是添加datavw的栏目名称============================================================
    datavw.ColumnHeaders.Add , , "五级编码", intwidth
    datavw.ColumnHeaders.Add , , "冰川编码", intwidth
    datavw.ColumnHeaders.Add , , "冰川名称", intwidth
    datavw.ColumnHeaders.Add , , "经度", intwidth
    datavw.ColumnHeaders.Add , , "纬度", intwidth
    datavw.ColumnHeaders.Add , , "地图类型", intwidth
    datavw.ColumnHeaders.Add , , "地图出版年代", intwidth
    datavw.ColumnHeaders.Add , , "地图比例尺", intwidth
    datavw.ColumnHeaders.Add , , "影像类型", intwidth
    datavw.ColumnHeaders.Add , , "影像比例尺", intwidth
    datavw.ColumnHeaders.Add , , "影像年代", intwidth
    datavw.ColumnHeaders.Add , , "总面积", intwidth
    datavw.ColumnHeaders.Add , , "面积精度", intwidth
    datavw.ColumnHeaders.Add , , "裸露区面积", intwidth
    datavw.ColumnHeaders.Add , , "消融区面积", intwidth
    datavw.ColumnHeaders.Add , , "平均宽度", intwidth
    datavw.ColumnHeaders.Add , , "平均长度", intwidth
    datavw.ColumnHeaders.Add , , "总长度", intwidth
    datavw.ColumnHeaders.Add , , "积累区长度", intwidth
    datavw.ColumnHeaders.Add , , "消融区长度", intwidth
    datavw.ColumnHeaders.Add , , "积累区朝向", intwidth
    datavw.ColumnHeaders.Add , , "消融区朝向", intwidth
    datavw.ColumnHeaders.Add , , "最高海拔", intwidth
    datavw.ColumnHeaders.Add , , "平均海拔", intwidth
    datavw.ColumnHeaders.Add , , "冰舌末端海拔", intwidth
    datavw.ColumnHeaders.Add , , "积累区最低海拔", intwidth
    datavw.ColumnHeaders.Add , , "冰川类型", intwidth
    datavw.ColumnHeaders.Add , , "冰碛类型", intwidth
    datavw.ColumnHeaders.Add , , "雪线高度", intwidth
    datavw.ColumnHeaders.Add , , "雪线高度精度", intwidth
    datavw.ColumnHeaders.Add , , "雪线测量日期", intwidth
    datavw.ColumnHeaders.Add , , "平均厚度", intwidth
    datavw.ColumnHeaders.Add , , "厚度精度", intwidth
    datavw.ColumnHeaders.Add , , "冰储量", intwidth
'==================================================================================
'****************************************************************************************
'************显示treeview控件中的树形结构
'****************************************************************************************
Dim indexn As Integer
Set t(0) = datatv.Nodes.Add(, , " 无", "中国冰川编目")
't(0).BackColor = (255)
t(0).ForeColor = 100
t(0).Expanded = True
Set tr(1) = datatv.Nodes.Add(, , "无", "流域名称")
tr(1).Bold = True
mdb
strec.Open "SELECT first.first_id,first.description FROM [first];", con, adOpenStatic, adLockPessimistic
Do While Not strec.EOF
    Set mnode = datatv.Nodes.Add(2, tvwChild, strec.Fields(0))
    mnode.Tag = "firstname"
    mnode.Text = strec.Fields(1)
   indexn = mnode.index
    strec.MoveNext
Loop

Command1.Caption = "检索内容"
List1.Height = 2550
Frame1.Visible = False
Frame1.Width = mapvw.Width
Frame1.Top = mapvw.Top
Frame1.Left = mapvw.Left
'*****************************************************************************************
'*****************添加listviews1栏目名称
'*******************************************************************************************
Dim ListName As Integer
ListName = ListView1.Width / 6
    ListView1.ColumnHeaders.Add , , "五级编码", ListName
    ListView1.ColumnHeaders.Add , , "冰川编码", intwidth
    ListView1.ColumnHeaders.Add , , "冰川名称", intwidth
    ListView1.ColumnHeaders.Add , , "经度", intwidth
    ListView1.ColumnHeaders.Add , , "纬度", intwidth
    ListView1.ColumnHeaders.Add , , "地图类型", intwidth
    ListView1.ColumnHeaders.Add , , "地图出版年代", intwidth
    ListView1.ColumnHeaders.Add , , "地图比例尺", intwidth
    ListView1.ColumnHeaders.Add , , "影像类型", intwidth
    ListView1.ColumnHeaders.Add , , "影像比例尺", intwidth
    ListView1.ColumnHeaders.Add , , "影像年代", intwidth
    ListView1.ColumnHeaders.Add , , "总面积", intwidth
    ListView1.ColumnHeaders.Add , , "面积精度", intwidth
    ListView1.ColumnHeaders.Add , , "裸露区面积", intwidth
    ListView1.ColumnHeaders.Add , , "消融区面积", intwidth
    ListView1.ColumnHeaders.Add , , "平均宽度", intwidth
    ListView1.ColumnHeaders.Add , , "平均长度", intwidth
    ListView1.ColumnHeaders.Add , , "总长度", intwidth
    ListView1.ColumnHeaders.Add , , "积累区长度", intwidth
    ListView1.ColumnHeaders.Add , , "消融区长度", intwidth
    ListView1.ColumnHeaders.Add , , "积累区朝向", intwidth
    ListView1.ColumnHeaders.Add , , "消融区朝向", intwidth
    ListView1.ColumnHeaders.Add , , "最高海拔", intwidth
    ListView1.ColumnHeaders.Add , , "平均海拔", intwidth
    ListView1.ColumnHeaders.Add , , "冰舌末端海拔", intwidth
    ListView1.ColumnHeaders.Add , , "积累区最低海拔", intwidth
    ListView1.ColumnHeaders.Add , , "冰川类型", intwidth
    ListView1.ColumnHeaders.Add , , "冰碛类型", intwidth
    ListView1.ColumnHeaders.Add , , "雪线高度", intwidth
    ListView1.ColumnHeaders.Add , , "雪线高度精度", intwidth
    ListView1.ColumnHeaders.Add , , "雪线测量日期", intwidth
    ListView1.ColumnHeaders.Add , , "平均厚度", intwidth
    ListView1.ColumnHeaders.Add , , "厚度精度", intwidth
    ListView1.ColumnHeaders.Add , , "冰储量", intwidth
'***********************************************************
'**********
'*********************************************************
    StatusBar1.Font = 3
End Sub


Private Sub Frame2_DragDrop(Source As Control, X As Single, Y As Single)

End Sub

Private Sub guanyuwomen_Click()
tongji.Checked = False
lingcunwei.Checked = False
dayin.Checked = False
chaxun.Checked = False
baobiao.Checked = False
neirong.Checked = False
guanyuwomen.Checked = True
End Sub

Private Sub Label1_Change()
mdb
ListView1.ListItems.Clear
    strec.Open "select * from glacier where GLACIER_ID='" & Label1.Caption & "'", con, adOpenStatic, adLockPessimistic
    listview_AddItem strec
End Sub

Private Sub lingcunwei_Click()
If SSTab1.Tab = 1 Then
    frmexport.Show
Else
    FrmSave.Show
End If
End Sub

Private Sub List1_Click()
Dim exp As String
Dim currec As MapObjects2.Recordset
exp = "glacier='" & List1 & "'"
Set schpoly = mapvw.Layers("冰川").SearchExpression(exp)
If Not schpoly.EOF Then
    Set shappoly = schpoly.Fields("shape").Value
    Set rect = shappoly.Extent
    rect.ScaleRectangle 6.5
    Set frmmain.mapvw.Extent = rect
    frmmain.mapvw.Refresh
End If
Frame1.Visible = False
'Label1.Visible = True
'Frame1.ZOrder 0
'Label1.Caption = List1.Text + " 的详细内容"
'***********************************************************************************************
'*****************点击冰川编目时显示详细内容
'***********************************************************************************************
'mdb
'ListView1.ListItems.Clear
'strec.Open "select * from glacier where GLACIER_ID='" & List1.Text & "'", con, adOpenStatic, adLockPessimistic
'listview_AddItem strec
End Sub

Private Sub maple_AfterSetLayerVisible(index As Integer, isVisible As Boolean)
mapvw.Refresh
End Sub

Private Sub maple_LayerDblClick(index As Integer)
Set oblayer = mapvw.Layers(index)
layercolor.Show vbModal
End Sub


Private Sub mapvw_AfterTrackingLayerDraw(ByVal hDC As stdole.OLE_HANDLE)
'*************************************************************************************
'***************在地图上画图后图形显示状态
'***************************************************************************************
Dim sym As New MapObjects2.Symbol
Dim typetext As New MapObjects2.TextSymbol
If Not re Is Nothing Then
    sym.Style = 1
    sym.OutlineColor = moRed
    sym.Size = 2
    mapvw.DrawShape re, sym
    Set re = Nothing
ElseIf Not el Is Nothing Then
    sym.Style = 1
    sym.OutlineColor = moRed
    sym.Size = 2
    mapvw.DrawShape el, sym
    Set el = Nothing
ElseIf Not po Is Nothing Then
    sym.Style = 1
    sym.OutlineColor = moRed
    sym.Size = 2
    mapvw.DrawShape po, sym
    Set po = Nothing
End If
'*****************************************************************************
'***********检索到单一目标时显示的状态
'****************************************************************************
If Not shappoly Is Nothing Then
    sym.Outline = True
    sym.Style = 7
    sym.Color = moRed
    mapvw.DrawShape shappoly, sym
End If
End Sub

Private Sub mapvw_MouseDown(Button As Integer, Shift As Integer, X As Single, Y As Single)
Dim tg As Double
Dim tl As MapObjects2.TrackingLayer
Set tl = mapvw.TrackingLayer
Dim fd As Double
Dim zoomOutRect As MapObjects2.Rectangle

tl.SymbolCount = 3
If Toolbar1.Buttons(15).Value = 1 Then
    Set zoomOutRect = mapvw.TrackRectangle
    fd = zoomOutRect.Width
    Set newrec = mapvw.Extent '设置放大为点击放大
    If fd > 0 Then
        Set mapvw.Extent = zoomOutRect
    Else
        mapwidth = mapvw.Extent.Width
        mapheight = mapvw.Extent.Height
        Set pot = mapvw.ToMapPoint(X, Y)
        newrec.Right = pot.X + (mapwidth * 0.35)
        newrec.Left = pot.X - (mapwidth * 0.35)
        newrec.Top = pot.Y + (mapheight * 0.35)
        newrec.Bottom = pot.Y - (mapheight * 0.35)
        mapvw.Extent = newrec
    End If
ElseIf Toolbar1.Buttons(14).Value = 1 Then
    mapvw.MousePointer = moPanning
    mapvw.Pan
    mapvw.MousePointer = moPan
ElseIf Toolbar1.Buttons(16).Value = 1 Then
    Set zoomOutRect = mapvw.TrackRectangle
    Set newrec = mapvw.Extent                '设置缩小为点击缩小
    mapwidth = mapvw.Extent.Width
    mapheight = mapvw.Extent.Height
    Set pot = mapvw.ToMapPoint(X, Y)
    newrec.Right = pot.X + (mapwidth * 0.55)
    newrec.Left = pot.X - (mapwidth * 0.55)
    newrec.Top = pot.Y + (mapheight * 0.55)
    newrec.Bottom = pot.Y - (mapheight * 0.55)
    mapvw.Extent = newrec
ElseIf Toolbar1.Buttons(11).Value = 1 Then
    List1.Clear
    Set re = mapvw.TrackRectangle
    For Each alayer In mapvw.Layers
        If alayer.Visible And alayer.LayerType = moMapLayer Then
            Set rec = alayer.SearchByDistance(re, 0, "")
            research
        End If
    Next alayer
    List1.Visible = True

ElseIf Toolbar1.Buttons(12).Value = 1 Then
    List1.Clear
    List1.Visible = True
    Set po = mapvw.TrackPolygon
    For Each alayer In mapvw.Layers
        If alayer.Visible And alayer.LayerType = moMapLayer Then
            Set rec = alayer.SearchByDistance(po, 0, "")
            research
        End If
    Next alayer
ElseIf Toolbar1.Buttons(13).Value = 1 Then
    Dim Npoint As New Point
    Dim layernamec As Variant
    Dim aDouble As Double
    Dim MRect As MapObjects2.Recordset
    layernamec = Array("河流", "冰川", "湖泊", "中国地图", "道路")
      Set Npoint = mapvw.ToMapPoint(X, Y)
      aDouble = mapvw.ToMapDistance(3 * Screen.TwipsPerPixelX)
      Set MRect = mapvw.Layers(layernamec(1)).SearchByDistance(Npoint, aDouble, "")
      Frame1.Visible = True
      If MRect.EOF Then
        Frame1.Visible = False
      Else
        Frame1.Visible = True
        Label1.Caption = MRect(layerName(1)).ValueAsString
      End If
End If
 mapvw.TrackingLayer.Refresh True
 End Sub

Private Sub mapvw_MouseMove(Button As Integer, Shift As Integer, X As Single, Y As Single)
If Toolbar1.Buttons(15).Value = 1 Then
    mapvw.MousePointer = moZoomIn
ElseIf Toolbar1.Buttons(16).Value = 1 Then
    mapvw.MousePointer = moZoomOut
ElseIf Toolbar1.Buttons(14).Value = 1 Then
    mapvw.MousePointer = moPan
ElseIf Toolbar1.Buttons(11).Value = 1 Or Toolbar1.Buttons(12).Value = 1 Then
    mapvw.MousePointer = moCross
ElseIf Toolbar1.Buttons(13).Value = 1 Then
    mapvw.MousePointer = moIdentify
End If
End Sub

Private Sub neirong_Click()
tongji.Checked = False
lingcunwei.Checked = False
dayin.Checked = False
chaxun.Checked = False
baobiao.Checked = False
neirong.Checked = True
guanyuwomen.Checked = False
help.Visible = True
End Sub

Private Sub Picture1_MouseDown(Button As Integer, Shift As Integer, X As Single, Y As Single)
Picture1.BackColor = 8421504
End Sub

Private Sub Picture1_MouseMove(Button As Integer, Shift As Integer, X As Single, Y As Single)
Picture1.ZOrder 0
Picture1.Refresh
If Button = 1 Then
    Command1.Width = SSTab1.Left + Picture1.Left
    List1.Width = SSTab1.Left + Picture1.Left
    Picture1.Left = Picture1.Left + X - 50
        If Picture1.Left > fm_l Then
                Picture1.Refresh
            Else
                Picture1.Left = fm_l
                Picture1_MouseUp Button, Shift, X, Y
        End If
End If
End Sub

Private Sub Picture1_MouseUp(Button As Integer, Shift As Integer, X As Single, Y As Single)
Picture1.BackColor = frmmain.BackColor
If SSTab1.Tab = 0 Then
    SSTab1.Width = SSTab1.Left + Picture1.Left
    datatv.Width = SSTab1.Width
    datavw.Left = Picture1.Left + Picture1.Width
    datavw.Width = frmmain.Width - SSTab1.Width - Picture1.Width - 120
ElseIf SSTab1.Tab = 1 Then
    SSTab1.Width = SSTab1.Left + Picture1.Left
    maple.Width = SSTab1.Width
    mapvw.Left = Picture1.Left + Picture1.Width
    mapvw.Width = frmmain.Width - SSTab1.Width - Picture1.Width - 120
'    frmmain.Refresh
End If
End Sub

Private Sub Player_Click()
CommonDialog1.ShowColor
Player.BackColor = CommonDialog1.Color

End Sub

Private Sub Pline_Click()
CommonDialog1.ShowColor
Pline.BackColor = CommonDialog1.Color

End Sub

Private Sub SSTab1_Click(PreviousTab As Integer)
If SSTab1.Tab = 1 Then
xianshituceng.Checked = True
xianshishuxing.Checked = False
Dim s As String
    List1.Visible = False
    Frame1.Visible = False
    ttt
    maple.setMapSource frmmain.mapvw
    maple.LoadLegend True
    maple.ShowAllLegend
    
    datavw.Visible = False
    mapvw.Visible = True
    SSTab1.Width = 2175
    Picture1.Left = 2160
    datatv.Width = 2115
    datavw.Left = 2200
    datavw.Width = 8500
    maple.Width = 2100
'    maple.LayerVisible(0) = False
    Command1.Width = SSTab1.Width - 60
    maple.LayerVisible(2) = False
ElseIf SSTab1.Tab = 0 Then
    xianshituceng.Checked = False
    xianshishuxing.Checked = True
    datavw.Visible = True
    mapvw.Visible = False
    SSTab1.Width = 2175
    Picture1.Left = 2160
    mapvw.Left = 2200
    mapvw.Width = 8500
    tt
    End If
Frame1.Visible = False
End Sub

Private Sub tongji_Click()
tongji.Checked = True
lingcunwei.Checked = False
dayin.Checked = False
chaxun.Checked = False
baobiao.Checked = False
neirong.Checked = False
guanyuwomen.Checked = False
frmTongJi.Visible = True
End Sub

Private Sub Toolbar1_ButtonClick(ByVal Button As MSComctlLib.Button)
'***********************************************************************
'******************设置显示与隐藏工具条中11、12、两个按钮
'*************************************************************************
If Toolbar1.Buttons(10).Value = 1 Then
    Toolbar1.Buttons(11).Visible = True
    Toolbar1.Buttons(12).Visible = True
ElseIf Toolbar1.Buttons(13).Value = 1 Or Toolbar1.Buttons(14).Value = 1 Or Toolbar1.Buttons(15).Value = 1 Or Toolbar1.Buttons(16).Value = 1 Then
    Toolbar1.Buttons(11).Visible = False
    Toolbar1.Buttons(12).Visible = False
    List1.Visible = False
    Frame1.Visible = False
End If
If Button.index = 6 Then
    Set mapvw.Extent = mapvw.FullExtent
ElseIf Button.index = 8 Then
    Set newrec = mapvw.Extent
    newrec.ScaleRectangle 0.8
    mapvw.Extent = newrec.Extent
ElseIf Button.index = 9 Then
    Set newrec = mapvw.Extent
    newrec.ScaleRectangle 1.8
    mapvw.Extent = newrec.Extent
ElseIf Button.index = 7 Then
    Frmresult.Show
ElseIf Button.index = 4 Then
    SSTab1.Tab = 0
ElseIf Button.index = 1 Then
    lingcunwei_Click
End If
End Sub

Private Sub tuichu_Click()
End
End Sub

Private Sub xianshishuxing_Click()
SSTab1.Tab = 0
tt
xianshishuxing.Checked = True
xianshituceng.Checked = False
End Sub

Private Sub xianshituceng_Click()
xianshituceng.Checked = True
xianshishuxing.Checked = False
SSTab1.Tab = 1
ttt
'****************************************************************
'***********显示图例
'*****************************************************************
maple.setMapSource frmmain.mapvw
maple.LoadLegend True
maple.ShowAllLegend
End Sub

