VERSION 5.00
Begin VB.Form FrmSave 
   BorderStyle     =   3  'Fixed Dialog
   Caption         =   "保存为"
   ClientHeight    =   3315
   ClientLeft      =   5850
   ClientTop       =   4560
   ClientWidth     =   5325
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   MinButton       =   0   'False
   ScaleHeight     =   3315
   ScaleWidth      =   5325
   ShowInTaskbar   =   0   'False
   Begin VB.DirListBox Dir1 
      Height          =   1770
      Left            =   120
      TabIndex        =   9
      Top             =   480
      Width           =   1935
   End
   Begin VB.TextBox Text1 
      Height          =   375
      Left            =   1080
      TabIndex        =   8
      Text            =   "Text1"
      Top             =   2400
      Width           =   3015
   End
   Begin VB.ComboBox Combo1 
      Height          =   300
      Left            =   1080
      TabIndex        =   5
      Text            =   "*.xls"
      Top             =   2880
      Width           =   3015
   End
   Begin VB.DriveListBox Drive 
      Height          =   300
      Left            =   720
      TabIndex        =   4
      Top             =   120
      Width           =   2415
   End
   Begin VB.FileListBox Filelist 
      Height          =   1710
      Left            =   2280
      TabIndex        =   3
      Top             =   480
      Width           =   2895
   End
   Begin VB.CommandButton CancelButton 
      Caption         =   "取消"
      Height          =   375
      Left            =   4200
      TabIndex        =   1
      Top             =   2880
      Width           =   975
   End
   Begin VB.CommandButton OKButton 
      Caption         =   "确定"
      Height          =   375
      Left            =   4200
      TabIndex        =   0
      Top             =   2400
      Width           =   975
   End
   Begin VB.Label Label3 
      Alignment       =   1  'Right Justify
      AutoSize        =   -1  'True
      Caption         =   "文件名："
      Height          =   180
      Left            =   120
      TabIndex        =   7
      Top             =   2520
      Width           =   720
   End
   Begin VB.Label Label2 
      Alignment       =   1  'Right Justify
      AutoSize        =   -1  'True
      Caption         =   "保存类型："
      Height          =   180
      Left            =   120
      TabIndex        =   6
      Top             =   3000
      Width           =   900
   End
   Begin VB.Label Label1 
      AutoSize        =   -1  'True
      Caption         =   "保存在"
      Height          =   300
      Left            =   120
      TabIndex        =   2
      Top             =   120
      Width           =   540
   End
End
Attribute VB_Name = "FrmSave"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Public oExcel As Object
Public oBook As Object
Public oSheet As Object
'Dim MyXlsApp As Object


Private Sub CancelButton_Click()
FrmSave.Hide
End Sub
Private Sub Dir1_Change()
Filelist.Path = Dir1.Path
End Sub

Private Sub Drive_Change()
Dir1.Path = Drive.Drive
End Sub

Private Sub OKButton_Click()
Dim Filename As String
'Set MyXlsApp = CreateObject("Excel.Application")

'MyXlsApp.Visible = True

Set oExcel = CreateObject("Excel.Application")
Set oBook = oExcel.Workbooks.Add
Set oSheet = oBook.Worksheets(1)
If frmmain.rsGlacier.RecordCount < 1 Then
MsgBox "请选择存储冰川范围！", vbYesNo
Else
oSheet.Range("A1").CopyFromRecordset frmmain.rsGlacier
'oSheet.range("A1").Value = 34.23
'注释：Save the Workbook and Quit Excel
Filename = "D:/" & Text1.Text & ".xls"
oBook.saveas Filename
MsgBox "文件储存完毕！", vbYesNo

oExcel.Quit
End If
Set oSheet = Nothing
Set oBook = Nothing
Set oExcel = Nothing
FrmSave.Refresh
End Sub
