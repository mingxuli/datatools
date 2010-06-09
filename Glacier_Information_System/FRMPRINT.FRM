VERSION 5.00
Object = "{F9043C88-F6F2-101A-A3C9-08002B2F49FB}#1.2#0"; "COMDLG32.OCX"
Begin VB.Form frmprint 
   Caption         =   "打印属性数据"
   ClientHeight    =   1890
   ClientLeft      =   7140
   ClientTop       =   4560
   ClientWidth     =   3435
   ControlBox      =   0   'False
   Icon            =   "frmprint.frx":0000
   LinkTopic       =   "Form1"
   ScaleHeight     =   1890
   ScaleWidth      =   3435
   Begin VB.CommandButton prcomno 
      Caption         =   "取消"
      Height          =   375
      Left            =   2160
      TabIndex        =   3
      Top             =   1080
      Width           =   1095
   End
   Begin VB.CommandButton prcomok 
      Caption         =   "确定"
      Height          =   375
      Left            =   240
      TabIndex        =   2
      Top             =   1080
      Width           =   1215
   End
   Begin VB.CommandButton prcomlog 
      Caption         =   "....."
      Height          =   375
      Left            =   2640
      TabIndex        =   1
      Top             =   480
      Width           =   615
   End
   Begin VB.TextBox prjpgname 
      Height          =   375
      Left            =   120
      Locked          =   -1  'True
      TabIndex        =   0
      Top             =   480
      Width           =   2295
   End
   Begin MSComDlg.CommonDialog CommonDialog1 
      Left            =   2640
      Top             =   120
      _ExtentX        =   847
      _ExtentY        =   847
      _Version        =   393216
   End
   Begin VB.Label Label4 
      Caption         =   "打印数据名称："
      Height          =   375
      Left            =   120
      TabIndex        =   4
      Top             =   120
      Width           =   1695
   End
End
Attribute VB_Name = "frmprint"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Form_Load()
If frmmain.SSTab1.Tab = 0 Then
    prjpgname.Text = "glacier.mdb"
    frmprint.Caption = "打印属性数据"
    Label4.Caption = "打印属性数据名称"
    CommonDialog1.Filter = "Access Files (*.mdb)|*.mdb"
    CommonDialog1.FileName = "glacier.mdb"
Else
    prjpgname.Text = "glacier.jpg"
    frmprint.Caption = " 打印图像"
    Label4.Caption = "打印图像名称"
    CommonDialog1.DialogTitle = "打印图像"
    CommonDialog1.Filter = "Jpeg Files (*.jpg)|*.jpg"
    CommonDialog1.FileName = "glacier.jpg"
End If
End Sub

Private Sub prcomlog_Click()
  CommonDialog1.Flags = cdlOFNOverwritePrompt Or cdlOFNExplorer
  CommonDialog1.Filter = "Print File (*.prn)|*.prn"
  CommonDialog1.DialogTitle = "打印"
  CommonDialog1.FileName = "glacier.prn"
  CommonDialog1.ShowSave
  prjpgname.Text = CommonDialog1.FileName
End Sub

Private Sub prcomno_Click()
Unload Me
End Sub

