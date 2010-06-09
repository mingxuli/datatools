Attribute VB_Name = "Module1"
Option Explicit
'****************************************************************************
'**************
'**************设置数据路径为相对路径**************************************xiaoge
'**************
'****************************************************************************

Public Function spath(pt As String) As String
Dim spp As String
spp = App.Path
spath = spp + "\" + pt
End Function
