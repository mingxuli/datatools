VERSION 5.00
Object = "{CDE57A40-8B86-11D0-B3C6-00A0C90AEA82}#1.0#0"; "MSDATGRD.OCX"
Begin VB.Form Frmresult 
   BorderStyle     =   3  'Fixed Dialog
   Caption         =   "中国冰川编目查询"
   ClientHeight    =   5970
   ClientLeft      =   45
   ClientTop       =   435
   ClientWidth     =   8415
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   MinButton       =   0   'False
   ScaleHeight     =   5970
   ScaleWidth      =   8415
   ShowInTaskbar   =   0   'False
   StartUpPosition =   3  '窗口缺省
   Begin VB.TextBox Text1 
      Height          =   270
      Left            =   6120
      TabIndex        =   13
      Text            =   "Text1"
      Top             =   5280
      Width           =   975
   End
   Begin MSDataGridLib.DataGrid DataGrid1 
      Height          =   3375
      Left            =   0
      TabIndex        =   8
      Top             =   1680
      Width           =   8295
      _ExtentX        =   14631
      _ExtentY        =   5953
      _Version        =   393216
      AllowUpdate     =   0   'False
      HeadLines       =   1
      RowHeight       =   15
      BeginProperty HeadFont {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "宋体"
         Size            =   9
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "宋体"
         Size            =   9
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ColumnCount     =   2
      BeginProperty Column00 
         DataField       =   ""
         Caption         =   ""
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   0
            Format          =   ""
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   2052
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column01 
         DataField       =   ""
         Caption         =   ""
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   0
            Format          =   ""
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   2052
            SubFormatType   =   0
         EndProperty
      EndProperty
      SplitCount      =   1
      BeginProperty Split0 
         BeginProperty Column00 
         EndProperty
         BeginProperty Column01 
         EndProperty
      EndProperty
   End
   Begin VB.CommandButton CmdSearch 
      Caption         =   "查  询"
      Height          =   375
      Left            =   6600
      TabIndex        =   7
      Top             =   1200
      Width           =   1335
   End
   Begin VB.ComboBox SearchField1 
      Height          =   300
      Left            =   4920
      TabIndex        =   3
      Top             =   840
      Width           =   3015
   End
   Begin VB.ComboBox Cmboperator1 
      Height          =   300
      Left            =   3240
      TabIndex        =   2
      Top             =   840
      Width           =   1575
   End
   Begin VB.ComboBox CmbItem1 
      Height          =   300
      Left            =   120
      TabIndex        =   1
      Top             =   840
      Width           =   3015
   End
   Begin VB.Label Label9 
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   10.5
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   0
      TabIndex        =   12
      Top             =   5400
      Width           =   2655
   End
   Begin VB.Label Label8 
      Caption         =   "字段英文名称："
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   10.5
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   2760
      TabIndex        =   11
      Top             =   1320
      Width           =   1695
   End
   Begin VB.Label Label7 
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   10.5
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   4560
      TabIndex        =   10
      Top             =   1320
      Width           =   1935
   End
   Begin VB.Label Label6 
      Caption         =   "查询结果："
      Height          =   375
      Left            =   120
      TabIndex        =   9
      Top             =   1275
      Width           =   2295
   End
   Begin VB.Label Label4 
      Caption         =   "运算符："
      Height          =   255
      Left            =   3120
      TabIndex        =   6
      Top             =   480
      Width           =   1695
   End
   Begin VB.Label Label3 
      Caption         =   "相应要素："
      Height          =   255
      Left            =   4920
      TabIndex        =   5
      Top             =   480
      Width           =   1215
   End
   Begin VB.Label Label2 
      Caption         =   "查询类型："
      Height          =   255
      Left            =   120
      TabIndex        =   4
      Top             =   600
      Width           =   1455
   End
   Begin VB.Label Label1 
      AutoSize        =   -1  'True
      Caption         =   "中国冰川编目查询"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   14.25
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   285
      Left            =   1920
      TabIndex        =   0
      Top             =   120
      Width           =   2400
   End
End
Attribute VB_Name = "Frmresult"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit
Dim ACon As ADODB.Connection
Dim rec As ADODB.Recordset
Dim dataname As Variant
Dim dataname1 As Variant
Dim i As Integer
Dim StrCon As String
Dim sumrec As ADODB.Recordset


'Private Sub Command1_Click()
''Set rec = New ADODB.Recordset
''Set ACon = New ADODB.Connection
''    StrCon = "provider=Microsoft.Jet.OLEDB.4.0;Data Source=GLACIER.mdb;"
''    ACon.Open StrCon
''
''Dim i As Integer
''    rec.Open "SELECT Sum(glacier.ICE_VOLUME)  FROM glacier;", ACon, adOpenStatic, adLockPessimistic
''    i = rec.Fields(0).Value
''    Text1.Text = i
'
''Text1.Text = DataGrid1
'End Sub

'Private Sub File1_Click()
'
'End Sub

Private Sub Form_Load()
Text1.Visible = False
dataname = Array("GLACIER_ID", "GLACIER_NA", "TOPO_TYPE", "TOPO_YEAR", "MAP_SCALE", "PHOTO_TYPE", "PHOTO_SCAL", "PHOTO_YEAR", "TOTAL_AREA", "AREA_ACCUR", "AREA_EXPOS", "AREA_ABLAT", "MEAN_WIDTH", "MEAN_LENGT", "TOTAL_LENG", "EXP_LENGTH", "ABL_LENGTH", "EXP_ORIEN", "ABL_ORIEN", "HIGH_ALTIT", "MEAN_ALTIT", "LOW_ALTITU", "EXP_LOW_AL", "GLA_CLASS", "MORAINE", "SNOWLINE", "SNOWL_ACCU", "SNOWL_DATE", "MEAN_DEPTH", "DEPTH_ACCU", "ICE_VOLUME")
dataname1 = Array("冰川编码", "冰川名称", "地图类型", "地图出版年代", "地图比例尺", "影像类型", "影像比例尺", "影像年代", "总面积(平方公里)", "面积精度", "裸露区面积(平方公里)", "消融区面积(平方公里)", "平均宽度(公里)", "平均长度(公里)", "总长度(公里)", "积累区长度(公里)", "消融区长度(公里)", "积累区朝向", "消融区朝向", "最高海拔(米)", "平均海拔(米)", "冰舌末端最低海拔(米)", "积累区最低海拔(米)", "冰川类型", "冰碛类型", "雪线高度(米)", "雪线高度精度", "雪线测量日期", "平均厚度", "厚度精度", "冰储量(立方公里)")
Dim intwidth As String
For i = 0 To 30
CmbItem1.AddItem dataname1(i)
Next i
End Sub
Private Sub CmbItem1_Click()
Set ACon = New ADODB.Connection
Set rec = New ADODB.Recordset
    Cmboperator1.Text = "="
    StrCon = "provider=Microsoft.Jet.OLEDB.4.0;Data Source=GLACIER.mdb;"
    ACon.Open StrCon
    rec.Open "select * from glacier", ACon, adOpenStatic, adLockPessimistic
SearchField1.Clear
If CmbItem1.Text = (dataname1(0)) Then
    SearchField1.Text = "5A254F0001"
    Label7.Caption = dataname(0)
    Do While Not rec.EOF
        SearchField1.AddItem rec.Fields(1)
    rec.MoveNext
    Loop
ElseIf CmbItem1.Text = (dataname1(1)) Then
    SearchField1.Text = "哈拉斯冰川"
    Label7.Caption = dataname(1)
    Do While Not rec.EOF
        If IsNull(rec.Fields(2).Value) = False Then
            SearchField1.AddItem rec.Fields(2)
        End If
        rec.MoveNext
    Loop
ElseIf CmbItem1.Text = (dataname1(2)) Then
    Label7.Caption = dataname(2)
        SearchField1.Text = "AM"
        SearchField1.AddItem "AM"
        SearchField1.AddItem "TM"
        SearchField1.AddItem "AM,TM"
        SearchField1.AddItem "AM；TM"
        SearchField1.AddItem "AM  TM"
ElseIf CmbItem1.Text = dataname1(3) Then
    Label7.Caption = dataname(3)
    SearchField1.Text = "请输入1910年-1985年之间的年代"
    Cmboperator1.AddItem "="
    Cmboperator1.AddItem ">"
    Cmboperator1.AddItem "<"
    Cmboperator1.AddItem "<="
    Cmboperator1.AddItem ">="
ElseIf CmbItem1.Text = dataname1(7) Then
    Label7.Caption = dataname(7)
    SearchField1.Text = "请输入1910年-1986年之间的年代"
    Cmboperator1.AddItem "="
    Cmboperator1.AddItem ">"
    Cmboperator1.AddItem "<"
    Cmboperator1.AddItem "<="
    Cmboperator1.AddItem ">="
End If
For i = 8 To 16
If CmbItem1.Text = dataname1(i) Then
    Label7.Caption = dataname(i)
    Cmboperator1.AddItem "="
    Cmboperator1.AddItem ">"
    Cmboperator1.AddItem "<"
    Cmboperator1.AddItem "<="
    Cmboperator1.AddItem ">="
End If
Next
For i = 19 To 30
If CmbItem1.Text = dataname1(i) Then
    Label7.Caption = dataname(i)
    Cmboperator1.AddItem "="
    Cmboperator1.AddItem ">"
    Cmboperator1.AddItem "<"
    Cmboperator1.AddItem "<="
    Cmboperator1.AddItem ">="
End If
Next
If CmbItem1.Text = dataname1(4) Then
    SearchField1.AddItem "1:9"
    SearchField1.AddItem "1:8"
    SearchField1.AddItem "1:7"
    SearchField1.AddItem "1:6,1:5"
    SearchField1.AddItem "1:6"
    SearchField1.AddItem "1:5,1:5"
    SearchField1.AddItem "1:5，1:5"
    SearchField1.AddItem "1:5,1:4"
    SearchField1.AddItem "1:5,1:10"
    SearchField1.AddItem "1:5  1:10"
    SearchField1.AddItem "1:5"
    SearchField1.AddItem "1:20"
    SearchField1.AddItem "1:11,1:6"
    SearchField1.AddItem "1:11"
    SearchField1.AddItem "1:10,1:5"
    SearchField1.AddItem "1:10  1:5"
    SearchField1.AddItem "1:10   1:5"
    SearchField1.AddItem "1:10    1:5"
    SearchField1.AddItem "1:10     1:5"
    SearchField1.AddItem "1:10"
ElseIf CmbItem1.Text = dataname1(5) Then
    SearchField1.AddItem "TP"
    SearchField1.AddItem "SP,AP"
    SearchField1.AddItem "SP"
    SearchField1.AddItem "AP,SP"
    SearchField1.AddItem "AP"
ElseIf CmbItem1.Text = dataname1(6) Then
    SearchField1.AddItem "1:7,1:6"
    SearchField1.AddItem "1:7"
    SearchField1.AddItem "1:6.5"
    SearchField1.AddItem "1:6,1:4"
    SearchField1.AddItem "1:6,1:10"
    SearchField1.AddItem "1:6"
    SearchField1.AddItem "1:50"
    SearchField1.AddItem "1:5.5"
    SearchField1.AddItem "1:5.4"
    SearchField1.AddItem "1:5.1"
    SearchField1.AddItem "1:5,1:6"
    SearchField1.AddItem "1:5,1:11"
    SearchField1.AddItem "1:5,1:10"
    SearchField1.AddItem "1:5       1:6"
    SearchField1.AddItem "1:5"
    SearchField1.AddItem "1:4.9"
    SearchField1.AddItem "1:4.7"
    SearchField1.AddItem "1:4.6"
    SearchField1.AddItem "1:4.5"
    SearchField1.AddItem "1:4.4"
    SearchField1.AddItem "1:4.3"
    SearchField1.AddItem "1:4.2"
    SearchField1.AddItem "1:4.1"
    SearchField1.AddItem "1:4,1:6"
    SearchField1.AddItem "1:4,1:5"
    SearchField1.AddItem "1:4"
    SearchField1.AddItem "1:3.9"
    SearchField1.AddItem "1:3.7"
    SearchField1.AddItem "1:3.2"
    SearchField1.AddItem "1:3"
    SearchField1.AddItem "1:2.8"
    SearchField1.AddItem "1:12,1:5"
    SearchField1.AddItem "1:12"
    SearchField1.AddItem "1:11,1:5"
    SearchField1.AddItem "1:11,1:10"
    SearchField1.AddItem "1:11"
    SearchField1.AddItem "1:100"
    SearchField1.AddItem "1:10,1:5"
    SearchField1.AddItem "1:10,1:11"
    SearchField1.AddItem "1:10"
ElseIf CmbItem1.Text = dataname1(17) Then
    Label7.Caption = dataname(17)
    SearchField1.AddItem "W."
    SearchField1.AddItem "W"
    SearchField1.AddItem "SW"
    SearchField1.AddItem "SE"
    SearchField1.AddItem "S."
    SearchField1.AddItem "S"
    SearchField1.AddItem "NW"
    SearchField1.AddItem "NE"
    SearchField1.AddItem "N"
    SearchField1.AddItem "E."
    SearchField1.AddItem "E"
    SearchField1.AddItem "7.6"
    SearchField1.AddItem "6"
    SearchField1.AddItem "2.9"
    SearchField1.AddItem "2.8"
    SearchField1.AddItem "2.7"
    SearchField1.AddItem "18.2"
    SearchField1.AddItem "1.7"
    SearchField1.AddItem "1.6"
    SearchField1.AddItem "1.5"
    SearchField1.AddItem "1.4"
    SearchField1.AddItem "1.2"
    SearchField1.AddItem "1.1"
    SearchField1.AddItem "1"
    SearchField1.AddItem "0.8"
    SearchField1.AddItem "0.7"
    SearchField1.AddItem "0.6"
    SearchField1.AddItem "0.5"
    SearchField1.AddItem "0.3"
ElseIf CmbItem1.Text = dataname1(18) Then
    Label7.Caption = dataname(18)
    SearchField1.AddItem "WN"
    SearchField1.AddItem "W."
    SearchField1.AddItem "W"
    SearchField1.AddItem "SW"
    SearchField1.AddItem "SE"
    SearchField1.AddItem "S5"
    SearchField1.AddItem "S"
    SearchField1.AddItem "NW"
    SearchField1.AddItem "NS"
    SearchField1.AddItem "NE"
    SearchField1.AddItem "N"
    SearchField1.AddItem "MW"
    SearchField1.AddItem "EW"
    SearchField1.AddItem "E."
    SearchField1.AddItem "E"
    SearchField1.AddItem "7.6"
    SearchField1.AddItem "5.7"
    SearchField1.AddItem "2.9"
    SearchField1.AddItem "2.8"
    SearchField1.AddItem "2.7"
    SearchField1.AddItem "18.2"
    SearchField1.AddItem "1.7"
    SearchField1.AddItem "1.6"
    SearchField1.AddItem "1.5"
    SearchField1.AddItem "1.4"
    SearchField1.AddItem "1.2"
    SearchField1.AddItem "1.1"
    SearchField1.AddItem "1"
    SearchField1.AddItem "0.8"
    SearchField1.AddItem "0.7"
    SearchField1.AddItem "0.6"
    SearchField1.AddItem "0.5"
End If
End Sub


Private Sub CmdExit_Click()
Unload Me
End Sub

Private Sub CmdSearch_Click()
Set ACon = New ADODB.Connection
Set rec = New ADODB.Recordset
Set sumrec = New ADODB.Recordset
Dim ing As Double
     StrCon = "provider=Microsoft.Jet.OLEDB.4.0;Data Source=GLACIER.mdb;"
    ACon.Open "FILEDSN=ge"
If CmbItem1.Text = dataname1(0) Then
    rec.Open "select * from glacier where " & dataname(0) & "='" & SearchField1.Text & "'", ACon, adOpenStatic, adLockPessimistic
    Set Me.DataGrid1.DataSource = rec
    ing = rec.RecordCount
    Label9.Caption = "搜索到冰川：" & ing & "条"
ElseIf CmbItem1.Text = dataname1(1) Then
    rec.Open "select * from glacier where " & dataname(1) & "='" & SearchField1.Text & "'", ACon, adOpenStatic, adLockPessimistic
    Set Me.DataGrid1.DataSource = rec
    ing = rec.RecordCount
    Label9.Caption = "搜索到冰川：" & ing & "条"
ElseIf CmbItem1.Text = dataname1(2) Then
    rec.Open "select * from glacier where " & dataname(2) & "='" & SearchField1.Text & "'", ACon, adOpenStatic, adLockPessimistic
    Set Me.DataGrid1.DataSource = rec
    ing = rec.RecordCount
    Label9.Caption = "搜索到冰川：" & ing & "条"
ElseIf CmbItem1.Text = dataname1(3) Then
    rec.Open "select * from glacier where " & dataname(3) & "" & Cmboperator1.Text & "'" & SearchField1.Text & "'", ACon, adOpenStatic, adLockPessimistic
    Set Me.DataGrid1.DataSource = rec
    ing = rec.RecordCount
    Label9.Caption = "搜索到冰川：" & ing & "条"
ElseIf CmbItem1.Text = dataname1(4) Then
    rec.Open "select * from glacier where " & dataname(4) & "='" & SearchField1.Text & "'", ACon, adOpenStatic, adLockPessimistic
    Set Me.DataGrid1.DataSource = rec
    ing = rec.RecordCount
    Label9.Caption = "搜索到冰川：" & ing & "条"
ElseIf CmbItem1.Text = dataname1(5) Then
    rec.Open "select * from glacier where " & dataname(5) & "='" & SearchField1.Text & "'", ACon, adOpenStatic, adLockPessimistic
    Set Me.DataGrid1.DataSource = rec
    ing = rec.RecordCount
    Label9.Caption = "搜索到冰川：" & ing & "条"
ElseIf CmbItem1.Text = dataname1(6) Then
    rec.Open "select * from glacier where " & dataname(6) & "='" & SearchField1.Text & "'", ACon, adOpenStatic, adLockPessimistic
    Set Me.DataGrid1.DataSource = rec
    ing = rec.RecordCount
    Label9.Caption = "搜索到冰川：" & ing & "条"
ElseIf CmbItem1.Text = dataname1(17) Then
    rec.Open "select * from glacier where " & dataname(17) & "='" & SearchField1.Text & "'", ACon, adOpenStatic, adLockPessimistic
    Set Me.DataGrid1.DataSource = rec
    ing = rec.RecordCount
    Label9.Caption = "搜索到冰川：" & ing & "条"
ElseIf CmbItem1.Text = dataname1(18) Then
    rec.Open "select * from glacier where " & dataname(18) & "='" & SearchField1.Text & "'", ACon, adOpenStatic, adLockPessimistic
    Set Me.DataGrid1.DataSource = rec
    ing = rec.RecordCount
    Label9.Caption = "搜索到冰川：" & ing & "条"
End If
For i = 7 To 16
    If CmbItem1.Text = dataname1(i) Then
        rec.Open "select * from glacier where " & dataname(i) & "" & Cmboperator1.Text & "'" & SearchField1.Text & "'", ACon, adOpenStatic, adLockPessimistic
        Set Me.DataGrid1.DataSource = rec
        ing = rec.RecordCount
        sumrec.Open "select rec.Fields(11) from rec", ACon, adOpenStatic, adLockPessimistic
        i = sumrec.Fields(0).Value
        Text1.Text = i
        Label9.Caption = "搜索到冰川：" & ing & "条"
    End If
Next
For i = 19 To 30
    If CmbItem1.Text = dataname1(i) Then
        rec.Open "select * from glacier where " & dataname(i) & "" & Cmboperator1.Text & "'" & SearchField1.Text & "'", ACon, adOpenStatic, adLockPessimistic
        Set Me.DataGrid1.DataSource = rec
        ing = rec.RecordCount
        
        Label9.Caption = "搜索到冰川：" & ing & "条"
    End If
Next
End Sub

