VERSION 5.00
Begin VB.Form frmTongJi 
   BorderStyle     =   3  'Fixed Dialog
   Caption         =   "统计结果"
   ClientHeight    =   4275
   ClientLeft      =   45
   ClientTop       =   435
   ClientWidth     =   5115
   Icon            =   "frmTongJi.frx":0000
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   MinButton       =   0   'False
   ScaleHeight     =   4275
   ScaleWidth      =   5115
   ShowInTaskbar   =   0   'False
   Begin VB.ListBox List1 
      Height          =   240
      Left            =   1320
      TabIndex        =   3
      Top             =   3000
      Width           =   975
   End
   Begin VB.TextBox Text1 
      Height          =   495
      Left            =   720
      TabIndex        =   2
      Text            =   "Text1"
      Top             =   2040
      Width           =   3975
   End
   Begin VB.ComboBox Combo1 
      Height          =   300
      Left            =   360
      TabIndex        =   1
      Text            =   "Combo1"
      Top             =   1080
      Width           =   2535
   End
   Begin VB.Label Label1 
      Caption         =   "Label1"
      Height          =   375
      Left            =   120
      TabIndex        =   0
      Top             =   240
      Width           =   3375
   End
End
Attribute VB_Name = "frmTongJi"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Dim conc As ADODB.Connection
Dim strng As String
Dim strecrc As ADODB.Recordset

Sub datas()
Set conc = New ADODB.Connection
Set strecrc = New ADODB.Recordset
strng = "provider=Microsoft.Jet.OLEDB.4.0;Data Source=GLACIER.mdb;"
conc.Open strng
'strecrc.Open "select * from glacier", conc, adOpenStatic, adLockPessimistic
End Sub

Private Sub Combo1_Click()
Dim s As Integer
datas
strecrc.Open "SELECT Sum(glacier.ICE_VOLUME)  FROM glacier;", conc
s = strecrc.Fields(0).Value

If Combo1.Text = "总面积" Then
   Text1.Text = s
End If

End Sub

Private Sub Form_Load()
Combo1.AddItem "总面积"
Label1.Caption = "请输入统计类型"
End Sub
