VERSION 5.00
Object = "{F9043C88-F6F2-101A-A3C9-08002B2F49FB}#1.2#0"; "COMDLG32.OCX"
Begin VB.Form frmexport 
   BorderStyle     =   1  'Fixed Single
   ClientHeight    =   1965
   ClientLeft      =   4605
   ClientTop       =   4860
   ClientWidth     =   3390
   Icon            =   "frmexport.frx":0000
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   MinButton       =   0   'False
   ScaleHeight     =   1965
   ScaleWidth      =   3390
   Begin MSComDlg.CommonDialog CommonDialog1 
      Left            =   2640
      Top             =   120
      _ExtentX        =   847
      _ExtentY        =   847
      _Version        =   393216
   End
   Begin VB.TextBox jpgname 
      Height          =   375
      Left            =   120
      Locked          =   -1  'True
      TabIndex        =   3
      Top             =   600
      Width           =   2295
   End
   Begin VB.CommandButton comlog 
      Caption         =   "....."
      Height          =   375
      Left            =   2640
      TabIndex        =   2
      Top             =   600
      Width           =   615
   End
   Begin VB.CommandButton comok 
      Caption         =   "确定"
      Height          =   375
      Left            =   120
      TabIndex        =   1
      Top             =   1320
      Width           =   1215
   End
   Begin VB.CommandButton comno 
      Caption         =   "取消"
      Height          =   375
      Left            =   2160
      TabIndex        =   0
      Top             =   1320
      Width           =   1095
   End
   Begin VB.Label Label3 
      Caption         =   "输出数据名称："
      Height          =   375
      Left            =   120
      TabIndex        =   4
      Top             =   120
      Width           =   1695
   End
End
Attribute VB_Name = "frmexport"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub comlog_Click()
CommonDialog1.Flags = cdlOFNOverwritePrompt Or cdlOFNExplorer
CommonDialog1.ShowSave
If CommonDialog1.FileName = "" Then Exit Sub
jpgname.Text = CommonDialog1.FileName
End Sub

Private Sub comno_Click()
Unload Me
End Sub

Private Sub comok_Click()
jpgnamet = CommonDialog1.FileName
If frmmain.SSTab1.Tab = 0 Then
Else
    frmmain.mapvw.ExportMapToJpeg jpgnamet
End If
Unload frmexport
End Sub

Private Sub Form_Load()
jpgname.Text = CommonDialog1.FileName
If frmmain.SSTab1.Tab = 0 Then
    jpgname.Text = "glacierdata.mdb"
    frmexport.Caption = "输出属性数据"
    Label3.Caption = "输出属性数据名称和路径"
    CommonDialog1.DialogTitle = "输出属性数据"
    CommonDialog1.Filter = "Access Files (*.mdb)|*.mdb"
    CommonDialog1.FileName = "glacier.mdb"
Else
    jpgname.Text = "glacierjpg.jpg"
    frmexport.Caption = "输出图像"
    Label3.Caption = "输出图像名称和路径"
    CommonDialog1.DialogTitle = "输出图像"
    CommonDialog1.Filter = "Jpeg Files (*.jpg)|*.jpg"
    CommonDialog1.FileName = "glacier.jpg"
End If
End Sub

