'If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
'Find the sum of all the multiples of 3 or 5 below 1000.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Function multiple(x As Integer)
    If (x Mod 3 = 0) Or (x Mod 5 = 0) Then
        multiple = True
    Else
        multiple = False
    End If
End Function

Sub main()
    Dim i As Integer
    
    For i = 1 To 999
        b = multiple(i)
        If b = True Then
            Total = Total + i
        End If
    Next i
    MsgBox (Total)
End Sub


