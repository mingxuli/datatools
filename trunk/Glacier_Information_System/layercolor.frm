VERSION 5.00
Object = "{F9043C88-F6F2-101A-A3C9-08002B2F49FB}#1.2#0"; "COMDLG32.OCX"
Begin VB.Form layercolor 
   Caption         =   "layer"
   ClientHeight    =   4470
   ClientLeft      =   4530
   ClientTop       =   3720
   ClientWidth     =   4215
   ControlBox      =   0   'False
   Icon            =   "layercolor.frx":0000
   LinkTopic       =   "Form1"
   PaletteMode     =   1  'UseZOrder
   ScaleHeight     =   4470
   ScaleWidth      =   4215
   Begin VB.TextBox TSize 
      Height          =   375
      Left            =   2160
      TabIndex        =   12
      Text            =   "Text1"
      Top             =   3240
      Width           =   615
   End
   Begin VB.ComboBox Cblayer 
      Height          =   300
      Left            =   1800
      TabIndex        =   10
      Text            =   "Combo1"
      Top             =   2640
      Width           =   1815
   End
   Begin VB.CommandButton Command3 
      Caption         =   "确定"
      BeginProperty Font 
         Name            =   "仿宋_GB2312"
         Size            =   14.25
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   2760
      TabIndex        =   8
      Top             =   3840
      Width           =   1095
   End
   Begin VB.CommandButton Command2 
      Caption         =   "取消"
      BeginProperty Font 
         Name            =   "仿宋_GB2312"
         Size            =   14.25
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   1440
      TabIndex        =   7
      Top             =   3840
      Width           =   1095
   End
   Begin VB.CommandButton Command1 
      Caption         =   "显示"
      BeginProperty Font 
         Name            =   "仿宋_GB2312"
         Size            =   14.25
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   120
      TabIndex        =   6
      Top             =   3840
      Width           =   1095
   End
   Begin MSComDlg.CommonDialog CommonDialog1 
      Left            =   600
      Top             =   720
      _ExtentX        =   847
      _ExtentY        =   847
      _Version        =   393216
   End
   Begin VB.PictureBox Pline 
      Height          =   615
      Left            =   2760
      ScaleHeight     =   555
      ScaleWidth      =   675
      TabIndex        =   3
      Top             =   1800
      Width           =   735
   End
   Begin VB.PictureBox Player 
      Height          =   615
      Left            =   2760
      ScaleHeight     =   555
      ScaleWidth      =   675
      TabIndex        =   2
      Top             =   960
      Width           =   735
   End
   Begin VB.TextBox TName 
      Height          =   375
      Left            =   1200
      TabIndex        =   1
      Top             =   240
      Width           =   2535
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Caption         =   "边线大小："
      BeginProperty Font 
         Name            =   "仿宋_GB2312"
         Size            =   14.25
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   360
      TabIndex        =   11
      Top             =   3240
      Width           =   1815
   End
   Begin VB.Label Ltype 
      BackStyle       =   0  'Transparent
      Caption         =   "图层类型："
      BeginProperty Font 
         Name            =   "仿宋_GB2312"
         Size            =   14.25
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   360
      TabIndex        =   9
      Top             =   2640
      Width           =   1935
   End
   Begin VB.Label Lncolor 
      BackStyle       =   0  'Transparent
      Caption         =   "图层边线颜色："
      BeginProperty Font 
         Name            =   "仿宋_GB2312"
         Size            =   15
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   360
      TabIndex        =   5
      Top             =   1920
      Width           =   2295
   End
   Begin VB.Label Lycolor 
      BackStyle       =   0  'Transparent
      Caption         =   "图层颜色："
      BeginProperty Font 
         Name            =   "仿宋_GB2312"
         Size            =   15
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   360
      TabIndex        =   4
      Top             =   1200
      Width           =   2175
   End
   Begin VB.Label lyname 
      BackStyle       =   0  'Transparent
      Caption         =   "Layer:"
      BeginProperty Font 
         Name            =   "仿宋_GB2312"
         Size            =   14.25
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   120
      TabIndex        =   0
      Top             =   240
      Width           =   1215
   End
End
Attribute VB_Name = "layercolor"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Dim lay As MapObjects2.MapLayer
Dim layerfill(7) As String
Dim linetype(4) As String
Dim recss As MapObjects2.Recordset
Sub combotext()

End Sub


Private Sub Command1_Click()
Dim sym As MapObjects2.Symbol
Set sym = lay.Symbol
Set lay.Renderer = Nothing
lay.Name = TName.Text
Select Case lay.shapeType
    Case moShapeTypePolygon
        sym.Style = Cblayer.ListIndex
        sym.Color = Player.BackColor
        sym.OutlineColor = Pline.BackColor
        If IsNumeric(TSize.Text) Then
            sym.Size = TSize.Text
        Else
            TSize.Text = 1
            sym.Size = 1
        End If
    Case moShapeTypeLine
        sym.Style = Cblayer.ListIndex
        sym.Color = Player.BackColor
        If IsNumeric(TSize.Text) Then
            sym.Size = TSize.Text
        Else
            TSize.Text = 1
            sym.Size = 1
        End If
        
End Select
frmmain.maple.LoadLegend
frmmain.mapvw.Refresh
End Sub

Private Sub Command2_Click()
Unload Me
End Sub

Private Sub Command3_Click()
Call Command1_Click
Unload Me
End Sub

Private Sub Form_Load()
Dim i As Integer
Set lay = frmmain.oblayer
layerfill(0) = "固体填充"
layerfill(1) = "透明填充"
layerfill(2) = "水平线填充"
layerfill(3) = "垂直线填充"
layerfill(4) = "上斜线填充"
layerfill(5) = "下斜线填充"
layerfill(6) = "正十字填充"
layerfill(7) = "斜十字填充"
linetype(0) = "实体线"
linetype(1) = "长线段虚线"
linetype(2) = "短线段虚线"
linetype(3) = "边界线虚线"
linetype(4) = "花虚线"
Set lay = frmmain.oblayer
Set recss = lay.Records
If lay.shapeType = moShapeTypeLine Then
    Pline.Enabled = False
    Lncolor.Enabled = False
    Cblayer.Text = linetype(0)
    For i = 0 To 4
        Cblayer.AddItem linetype(i)
    Next i
Else
    Pline.Enabled = True
    Cblayer.Text = layerfill(0)
    For i = 0 To 7
        Cblayer.AddItem layerfill(i)
    Next i
        Lncolor.Enabled = True
    End If
TName.Text = lay.Name
Player.BackColor = lay.Symbol.Color
Pline.BackColor = lay.Symbol.OutlineColor
Cblayer.ListIndex = lay.Symbol.Style
TSize.Text = 1
End Sub

Private Sub Player_Click()
CommonDialog1.ShowColor
Player.BackColor = CommonDialog1.Color
End Sub

Private Sub Pline_Click()
CommonDialog1.ShowColor
Pline.BackColor = CommonDialog1.Color
End Sub

