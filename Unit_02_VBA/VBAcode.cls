
Sub Stocks()

    Dim LastRow As Long

    LastRow = Cells(Rows.Count, 1).End(xlUp).Row

  ' Set an initial variable for holding the brand name
  Dim Ticker As String

  ' Set an initial variable for holding the total per credit card brand
  Dim Volume_Total As Double
  Brand_Total = 0

  ' Keep track of the location for each credit card brand in the summary table
  Dim Summary_Table_Row As Integer
  Summary_Table_Row = 2

  ' Loop through all credit card purchases
  For i = 2 To LastRow

    ' Check if we are still within the same credit card brand, if it is not...
    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

      ' Set the Brand name
      Ticker = Cells(i, 1).Value

      ' Add to the Brand Total
      Volume_Total = Volume_Total + Cells(i, 7).Value

      ' Print the Credit Card Brand in the Summary Table
      Range("I" & Summary_Table_Row).Value = Ticker

      ' Print the Brand Amount to the Summary Table
      Range("J" & Summary_Table_Row).Value = Volume_Total

      ' Add one to the summary table row
      Summary_Table_Row = Summary_Table_Row + 1
      
      ' Reset the Brand Total
      Volume_Total = 0

    ' If the cell immediately following a row is the same brand...
    Else

      ' Add to the Brand Total
      Volume_Total = Volume_Total + Cells(i, 7).Value

    End If

  Next i

End Sub

